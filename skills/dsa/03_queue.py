"""
03 - Queue & Circular Queue
=============================
Implementations of standard Queue (FIFO) and Circular Queue with a
practical task scheduler simulation.

Key Concepts:
    - First-In, First-Out (FIFO) principle
    - Circular buffer technique
    - collections.deque for efficient queues
    - Real-world application: task scheduling
"""

from collections import deque


class Queue:
    """Standard queue using collections.deque for O(1) operations."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self._items.popleft()

    def front(self):
        """Peek at the front item without removing it."""
        if self.is_empty():
            raise IndexError("Front of an empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"Queue({list(self._items)})"


class CircularQueue:
    """Fixed-size circular queue using a list as a ring buffer."""

    def __init__(self, capacity):
        self._capacity = capacity
        self._buffer = [None] * capacity
        self._front = 0
        self._rear = -1
        self._size = 0

    def enqueue(self, item):
        """Add an item. Raises OverflowError if full."""
        if self.is_full():
            raise OverflowError("Circular queue is full")
        self._rear = (self._rear + 1) % self._capacity
        self._buffer[self._rear] = item
        self._size += 1

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty circular queue")
        item = self._buffer[self._front]
        self._buffer[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def __repr__(self):
        items = []
        idx = self._front
        for _ in range(self._size):
            items.append(self._buffer[idx])
            idx = (idx + 1) % self._capacity
        return f"CircularQueue(cap={self._capacity}, items={items})"


def task_scheduler_demo():
    """Simulate a round-robin task scheduler using a queue."""
    tasks = Queue()
    task_list = [
        {"name": "Download file", "time": 3},
        {"name": "Compile code", "time": 2},
        {"name": "Run tests", "time": 4},
        {"name": "Deploy app", "time": 1},
    ]

    for task in task_list:
        tasks.enqueue(task)

    print("--- Round-Robin Task Scheduler ---")
    time_slice = 1
    clock = 0

    while not tasks.is_empty():
        current = tasks.dequeue()
        clock += time_slice
        current["time"] -= time_slice
        print(f"  [t={clock}] Processing '{current['name']}' (remaining: {current['time']}s)")

        if current["time"] > 0:
            tasks.enqueue(current)
        else:
            print(f"         ✅ '{current['name']}' completed!")

    print(f"  All tasks finished at t={clock}")


if __name__ == "__main__":
    # --- Standard Queue ---
    q = Queue()
    for val in ["A", "B", "C", "D"]:
        q.enqueue(val)
    print(f"Queue: {q}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Front: {q.front()}")
    print(f"After dequeue: {q}")

    # --- Circular Queue ---
    print("\n--- Circular Queue ---")
    cq = CircularQueue(4)
    for val in [10, 20, 30, 40]:
        cq.enqueue(val)
    print(f"Full: {cq}")
    cq.dequeue()
    cq.dequeue()
    cq.enqueue(50)
    print(f"After 2 dequeues + enqueue 50: {cq}")

    # --- Scheduler ---
    print()
    task_scheduler_demo()
