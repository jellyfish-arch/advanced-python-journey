"""
05 - Hash Table (Separate Chaining)
=====================================
A hash table built from scratch using separate chaining for collision
resolution, with dynamic resizing when the load factor exceeds a threshold.

Key Concepts:
    - Hashing and hash functions
    - Collision resolution via chaining
    - Dynamic resizing / rehashing
    - Average O(1) lookup, insert, delete
"""


class HashTable:
    """Hash table using separate chaining."""

    def __init__(self, initial_capacity=8):
        self._capacity = initial_capacity
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]

    def _hash(self, key):
        return hash(key) % self._capacity

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        if self._size / self._capacity > 0.75:
            self._resize()

    def get(self, key, default=None):
        idx = self._hash(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        return default

    def delete(self, key):
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return True
        return False

    def contains(self, key):
        return self.get(key, object()) is not object()

    def keys(self):
        return [k for bucket in self._buckets for k, v in bucket]

    def items(self):
        return [(k, v) for bucket in self._buckets for k, v in bucket]

    def _resize(self):
        old_items = self.items()
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for key, value in old_items:
            self.put(key, value)

    def __len__(self):
        return self._size

    def __repr__(self):
        pairs = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return f"HashTable({{{pairs}}})"


if __name__ == "__main__":
    ht = HashTable()
    data = {"apple": 3, "banana": 5, "cherry": 7, "date": 2,
            "elderberry": 9, "fig": 1, "grape": 4, "honeydew": 6}
    for key, value in data.items():
        ht.put(key, value)

    print("--- Hash Table ---")
    print(f"Table: {ht}")
    print(f"Size: {len(ht)}")
    print(f"Get 'cherry': {ht.get('cherry')}")
    print(f"Get 'mango':  {ht.get('mango', 'NOT FOUND')}")

    ht.put("apple", 10)
    print(f"\nAfter updating 'apple': {ht.get('apple')}")

    ht.delete("banana")
    print(f"After deleting 'banana': Keys = {ht.keys()}")
    print(f"Final size: {len(ht)}")
