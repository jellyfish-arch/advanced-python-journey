"""
09 - Min-Heap & Priority Queue
================================
A min-heap built from scratch with insert, extract-min, and heapify,
plus a priority queue for task management.

Key Concepts:
    - Complete binary tree property
    - Heap ordering (min-heap)
    - Sift-up / sift-down operations
    - Priority queue pattern
"""


class MinHeap:
    """Min-Heap implementation using a list."""

    def __init__(self):
        self._data = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _sift_up(self, i):
        while i > 0 and self._data[i] < self._data[self._parent(i)]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _sift_down(self, i):
        size = len(self._data)
        smallest = i
        left = self._left(i)
        right = self._right(i)

        if left < size and self._data[left] < self._data[smallest]:
            smallest = left
        if right < size and self._data[right] < self._data[smallest]:
            smallest = right

        if smallest != i:
            self._swap(i, smallest)
            self._sift_down(smallest)

    def insert(self, value):
        """Insert a value into the heap."""
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def extract_min(self):
        """Remove and return the minimum element."""
        if not self._data:
            raise IndexError("Extract from empty heap")
        min_val = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return min_val

    def peek(self):
        """Return the minimum without removing it."""
        if not self._data:
            raise IndexError("Peek from empty heap")
        return self._data[0]

    def size(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    @classmethod
    def heapify(cls, arr):
        """Build a heap from an unsorted list in O(n)."""
        heap = cls()
        heap._data = arr[:]
        for i in range(len(heap._data) // 2 - 1, -1, -1):
            heap._sift_down(i)
        return heap

    def __repr__(self):
        return f"MinHeap({self._data})"


class PriorityQueue:
    """Priority queue using MinHeap — lower number = higher priority."""

    def __init__(self):
        self._heap = MinHeap()
        self._counter = 0  # tie-breaker for equal priorities

    def enqueue(self, item, priority):
        self._heap.insert((priority, self._counter, item))
        self._counter += 1

    def dequeue(self):
        if self._heap.is_empty():
            raise IndexError("Dequeue from empty priority queue")
        priority, _, item = self._heap.extract_min()
        return item, priority

    def peek(self):
        priority, _, item = self._heap.peek()
        return item, priority

    def is_empty(self):
        return self._heap.is_empty()

    def size(self):
        return self._heap.size()


if __name__ == "__main__":
    # --- Min-Heap ---
    print("--- Min-Heap ---")
    heap = MinHeap()
    for val in [35, 10, 25, 5, 40, 15, 30]:
        heap.insert(val)
    print(f"Heap: {heap}")
    print(f"Peek: {heap.peek()}")
    print(f"Extract min: {heap.extract_min()}")
    print(f"After extract: {heap}")

    # Heapify
    arr = [50, 20, 80, 10, 60, 30]
    built = MinHeap.heapify(arr)
    print(f"\nHeapify {arr} -> {built}")

    # Heap sort
    sorted_vals = []
    while not built.is_empty():
        sorted_vals.append(built.extract_min())
    print(f"Heap sort result: {sorted_vals}")

    # --- Priority Queue ---
    print("\n--- Priority Queue (Task Scheduler) ---")
    pq = PriorityQueue()
    tasks = [
        ("Fix critical bug", 1),
        ("Write docs", 4),
        ("Code review", 2),
        ("Deploy to staging", 3),
        ("Respond to email", 5),
    ]
    for task, pri in tasks:
        pq.enqueue(task, pri)

    print("Processing tasks by priority:")
    while not pq.is_empty():
        task, priority = pq.dequeue()
        print(f"  [{priority}] {task}")
