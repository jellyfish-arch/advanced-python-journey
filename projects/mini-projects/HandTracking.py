"""
hand_tracker.py
────────────────────────────────────────────────
Full finger tracking: count, gestures, movement trails
Dependencies: pip install mediapipe opencv-python
────────────────────────────────────────────────
"""

import cv2
import mediapipe as mp
import time
from collections import deque

# ── MediaPipe setup ──────────────────────────────────────────────────────────
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
mp_style = mp.solutions.drawing_styles

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6,
)

# ── Landmark indices ─────────────────────────────────────────────────────────
TIPS = [4, 8, 12, 16, 20]   # thumb, index, middle, ring, pinky tips
BASES = [2, 6, 10, 14, 18]   # corresponding MCP / IP joints for comparison
WRIST = 0

# ── Gesture definitions ──────────────────────────────────────────────────────


def fingers_up(lm, handedness):
    """Returns list [thumb, index, middle, ring, pinky] → 1=up, 0=down"""
    fingers = []

    # Thumb: compare tip x to IP joint x (flip for left hand)
    if handedness == "Right":
        fingers.append(1 if lm[4].x < lm[3].x else 0)
    else:
        fingers.append(1 if lm[4].x > lm[3].x else 0)

    # Other four fingers: tip y < PIP y → finger is up
    for tip, pip in zip(TIPS[1:], [7, 11, 15, 19]):
        fingers.append(1 if lm[tip].y < lm[pip].y else 0)

    return fingers


GESTURES = {
    # fingers:  [thumb, index, middle, ring, pinky]
    (0, 0, 0, 0, 0): "✊  Fist",
    (1, 1, 1, 1, 1): "🖐  Open Hand",
    (0, 1, 0, 0, 0): "☝  Pointing",
    (0, 1, 1, 0, 0): "✌  Peace / V",
    (1, 0, 0, 0, 0): "👍 Thumbs Up",
    (0, 0, 0, 0, 1): "🤙 Pinky Up",
    (1, 1, 0, 0, 1): "🤙 Shaka",
    (0, 1, 0, 0, 1): "🤘 Rock",
    (1, 1, 1, 0, 0): "3 Fingers",
    (0, 1, 1, 1, 0): "3 Fingers (mid)",
    (1, 0, 0, 0, 1): "Guns 🤟",
    (0, 1, 1, 1, 1): "4 Fingers",
    (1, 1, 0, 0, 0): "L-Shape",
    (1, 0, 1, 0, 0): "Pistol",
}


def classify_gesture(fingers):
    key = tuple(fingers)
    return GESTURES.get(key, f"{sum(fingers)} Finger{'s' if sum(fingers) != 1 else ''}")


# ── Trail buffers (one deque per hand index) ─────────────────────────────────
TRAIL_LEN = 30
trails = [deque(maxlen=TRAIL_LEN), deque(maxlen=TRAIL_LEN)]

# ── Color palette ────────────────────────────────────────────────────────────
COLORS = {
    "right": (0, 230, 120),   # green
    "left": (80, 160, 255),  # blue-ish
    "trail": (255, 80, 200),  # magenta trail
    "text": (255, 255, 255),
    "bg": (20, 20, 20),
}

# ── HUD helpers ──────────────────────────────────────────────────────────────


def put_text(img, text, pos, scale=0.7, color=(255, 255, 255), thickness=2):
    cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX,
                scale, (0, 0, 0), thickness+2)
    cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX,
                scale, color, thickness)


def draw_finger_dots(img, lm, w, h, color):
    for tip in TIPS:
        cx, cy = int(lm[tip].x * w), int(lm[tip].y * h)
        cv2.circle(img, (cx, cy), 10, color, -1)
        cv2.circle(img, (cx, cy),  10, (255, 255, 255), 2)


def draw_trail(img, trail, color):
    pts = list(trail)
    for i in range(1, len(pts)):
        alpha = i / len(pts)
        c = tuple(int(v * alpha) for v in color)
        cv2.line(img, pts[i-1], pts[i], c, 3)


# ── Main loop ────────────────────────────────────────────────────────────────
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

prev_time = 0

print("Hand Tracker running — press Q to quit")

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break

    frame = cv2.flip(frame, 1)           # mirror
    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)

    # ── Draw header bar ──────────────────────────────────────────────────────
    cv2.rectangle(frame, (0, 0), (w, 48), (30, 30, 30), -1)
    put_text(frame, "HAND TRACKER  |  Q = quit",
             (14, 32), scale=0.65, color=(180, 180, 180))

    # ── Process detected hands ───────────────────────────────────────────────
    active_trails = set()

    if res.multi_hand_landmarks:
        for idx, (hlm, hinfo) in enumerate(
            zip(res.multi_hand_landmarks, res.multi_handedness)
        ):
            side = hinfo.classification[0].label   # "Left" / "Right"
            color = COLORS["right"] if side == "Right" else COLORS["left"]
            lm = hlm.landmark

            # Skeleton
            mp_draw.draw_landmarks(
                frame, hlm,
                mp_hands.HAND_CONNECTIONS,
                mp_draw.DrawingSpec(
                    color=color,      thickness=2, circle_radius=3),
                mp_draw.DrawingSpec(color=(200, 200, 200), thickness=1),
            )

            # Fingertip dots
            draw_finger_dots(frame, lm, w, h, color)

            # Index-finger trail (tip landmark 8)
            ix = int(lm[8].x * w)
            iy = int(lm[8].y * h)
            trails[idx].append((ix, iy))
            active_trails.add(idx)
            draw_trail(frame, trails[idx], COLORS["trail"])

            # Finger state & gesture
            f_state = fingers_up(lm, side)
            gesture = classify_gesture(f_state)
            count = sum(f_state)

            # Per-hand info panel
            panel_y = 70 + idx * 130
            cv2.rectangle(frame, (8, panel_y - 24),
                          (320, panel_y + 100), (30, 30, 30), -1)
            cv2.rectangle(frame, (8, panel_y - 24),
                          (320, panel_y + 100), color, 2)

            put_text(frame, f"{side} Hand",   (16, panel_y),
                     scale=0.7,  color=color)
            put_text(
                frame, f"Fingers: {count}", (16, panel_y + 30), scale=0.65, color=COLORS["text"])
            put_text(frame, gesture,           (16, panel_y + 60),
                     scale=0.65, color=(255, 220, 80))

            # Finger state bar  [T I M R P]
            labels = ["T", "I", "M", "R", "P"]
            for fi, (lbl, state) in enumerate(zip(labels, f_state)):
                bx = 16 + fi * 44
                by = panel_y + 90
                bc = color if state else (80, 80, 80)
                cv2.rectangle(frame, (bx, by-18), (bx+36, by), bc, -1)
                put_text(frame, lbl, (bx+10, by-4), scale=0.45,
                         color=(0, 0, 0), thickness=1)

    # Clear stale trails for hands no longer detected
    for i in range(2):
        if i not in active_trails:
            trails[i].clear()

    # ── FPS counter ──────────────────────────────────────────────────────────
    cur_time = time.time()
    fps = 1 / max(cur_time - prev_time, 1e-6)
    prev_time = cur_time
    put_text(frame, f"FPS: {int(fps)}", (w - 110, 32),
             scale=0.65, color=(150, 255, 150))

    cv2.imshow("Hand Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Tracker closed.")
