# 09 - Collections Module
# Intermediate Concept: Specialized container types beyond basic lists and dicts

from collections import Counter, defaultdict, namedtuple, deque, OrderedDict, ChainMap

# --- Counter: Count occurrences ---
print("=" * 50)
print("COUNTER")
print("=" * 50)

# Count characters in a string
char_count = Counter("mississippi")
print(f"Character count: {char_count}")
print(f"Most common 3: {char_count.most_common(3)}")

# Count words in text
text = "python is great and python is fast and python is readable"
word_count = Counter(text.split())
print(f"\nWord count: {dict(word_count)}")

# Counter arithmetic
inventory_a = Counter(apples=5, oranges=3, bananas=2)
inventory_b = Counter(apples=2, oranges=5, grapes=4)
combined = inventory_a + inventory_b
difference = inventory_a - inventory_b
print(f"\nWarehouse A: {dict(inventory_a)}")
print(f"Warehouse B: {dict(inventory_b)}")
print(f"Combined:    {dict(combined)}")
print(f"A - B:       {dict(difference)}")

print()

# --- defaultdict: Dicts with default values ---
print("=" * 50)
print("DEFAULTDICT")
print("=" * 50)

# Group items by category
products = [
    ("Electronics", "Laptop"),
    ("Clothing", "T-Shirt"),
    ("Electronics", "Phone"),
    ("Food", "Rice"),
    ("Clothing", "Jeans"),
    ("Electronics", "Tablet"),
    ("Food", "Bread"),
]

grouped = defaultdict(list)
for category, item in products:
    grouped[category].append(item)

print("Grouped products:")
for category, items in grouped.items():
    print(f"  {category}: {', '.join(items)}")

# Count with defaultdict
letter_count = defaultdict(int)
for char in "abracadabra":
    letter_count[char] += 1
print(f"\nLetter count: {dict(letter_count)}")

# Nested defaultdict (adjacency list)
graph = defaultdict(list)
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
for src, dst in edges:
    graph[src].append(dst)
    graph[dst].append(src)

print(f"\nGraph adjacency list:")
for node, neighbors in sorted(graph.items()):
    print(f"  {node} -> {neighbors}")

print()

# --- namedtuple: Lightweight immutable objects ---
print("=" * 50)
print("NAMEDTUPLE")
print("=" * 50)

Point = namedtuple("Point", ["x", "y"])
Employee = namedtuple("Employee", "name department salary")

p1 = Point(3, 4)
p2 = Point(6, 8)
print(f"Point 1: {p1}")
print(f"Distance from origin: {(p1.x**2 + p1.y**2)**0.5:.2f}")

# Calculate distance between points
distance = ((p2.x - p1.x)**2 + (p2.y - p1.y)**2) ** 0.5
print(f"Distance {p1} -> {p2}: {distance:.2f}")

# Named tuples as lightweight records
team = [
    Employee("Arjun", "Engineering", 92000),
    Employee("Priya", "Design", 78000),
    Employee("Vikram", "Engineering", 88000),
    Employee("Meera", "Marketing", 71000),
]

print(f"\nTeam (sorted by salary):")
for emp in sorted(team, key=lambda e: e.salary, reverse=True):
    print(f"  {emp.name:<10} {emp.department:<15} Rs.{emp.salary:>8,}")

# _replace creates a new instance with updated values
promoted = team[0]._replace(salary=105000)
print(f"\nPromoted: {promoted}")

print()

# --- deque: Double-ended queue ---
print("=" * 50)
print("DEQUE")
print("=" * 50)

# Efficient append/pop from both ends
dq = deque([1, 2, 3, 4, 5])
print(f"Initial: {list(dq)}")

dq.appendleft(0)
dq.append(6)
print(f"After appendleft(0) & append(6): {list(dq)}")

dq.popleft()
dq.pop()
print(f"After popleft() & pop(): {list(dq)}")

dq.rotate(2)   # Rotate right by 2
print(f"After rotate(2): {list(dq)}")

dq.rotate(-2)  # Rotate left by 2
print(f"After rotate(-2): {list(dq)}")

# maxlen: bounded deque (sliding window)
recent_logs = deque(maxlen=3)
logs = ["Server started", "User login", "API call", "DB query", "User logout"]
for log in logs:
    recent_logs.append(log)
    print(f"  Added: '{log}' -> Recent: {list(recent_logs)}")

print()

# --- ChainMap: Layered dictionary lookups ---
print("=" * 50)
print("CHAINMAP")
print("=" * 50)

defaults = {"theme": "dark", "language": "en", "debug": False, "timeout": 30}
env_config = {"debug": True, "timeout": 60}
user_config = {"theme": "light"}

config = ChainMap(user_config, env_config, defaults)
print("Layered config (user > env > defaults):")
for key in ["theme", "language", "debug", "timeout"]:
    print(f"  {key}: {config[key]}")

print(f"\nFull resolved config: {dict(config)}")

print()

# --- Practical: Analyzing survey data ---
print("=" * 50)
print("PRACTICAL: Survey Analysis")
print("=" * 50)

survey_responses = [
    {"age_group": "18-25", "rating": 4, "platform": "mobile"},
    {"age_group": "26-35", "rating": 5, "platform": "web"},
    {"age_group": "18-25", "rating": 3, "platform": "mobile"},
    {"age_group": "36-45", "rating": 4, "platform": "web"},
    {"age_group": "26-35", "rating": 5, "platform": "mobile"},
    {"age_group": "18-25", "rating": 4, "platform": "web"},
    {"age_group": "36-45", "rating": 3, "platform": "web"},
    {"age_group": "26-35", "rating": 4, "platform": "mobile"},
]

# Group ratings by age
ratings_by_age = defaultdict(list)
for resp in survey_responses:
    ratings_by_age[resp["age_group"]].append(resp["rating"])

print("Average rating by age group:")
for age, ratings in sorted(ratings_by_age.items()):
    avg = sum(ratings) / len(ratings)
    print(f"  {age}: {avg:.1f}/5 ({len(ratings)} responses)")

# Platform distribution
platform_count = Counter(r["platform"] for r in survey_responses)
print(f"\nPlatform distribution: {dict(platform_count)}")


# --- Main ---
if __name__ == "__main__":
    print("\n--- Summary ---")
    print("Covered: Counter, defaultdict, namedtuple, deque, ChainMap")
    print("Key insight: collections module provides optimized, readable alternatives")
