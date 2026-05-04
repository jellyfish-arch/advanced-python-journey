"""
06 - Sorting Algorithms
========================
Side-by-side implementations of classic sorting algorithms with
performance comparison.

Key Concepts:
    - Bubble Sort, Selection Sort, Insertion Sort (O(n²))
    - Merge Sort, Quick Sort (O(n log n))
    - Stability and in-place sorting
    - Time complexity comparison
"""

import time
import random


def bubble_sort(arr):
    """Bubble Sort — O(n²) average, O(n) best (optimized)."""
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(arr):
    """Selection Sort — O(n²) in all cases."""
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr):
    """Insertion Sort — O(n²) average, O(n) best."""
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    """Merge Sort — O(n log n) in all cases, stable."""
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr):
    """Quick Sort — O(n log n) average, O(n²) worst."""
    if len(arr) <= 1:
        return arr[:]

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def benchmark(sort_func, data, name):
    """Time a sorting function and return the duration in ms."""
    start = time.perf_counter()
    result = sort_func(data)
    elapsed = (time.perf_counter() - start) * 1000
    return name, elapsed, result


if __name__ == "__main__":
    # Small demo
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("--- Sorting Algorithms ---")
    print(f"Original: {sample}\n")

    algorithms = [
        (bubble_sort, "Bubble Sort"),
        (selection_sort, "Selection Sort"),
        (insertion_sort, "Insertion Sort"),
        (merge_sort, "Merge Sort"),
        (quick_sort, "Quick Sort"),
    ]

    for func, name in algorithms:
        result = func(sample)
        print(f"  {name:20s} -> {result}")

    # Performance comparison
    print("\n--- Performance Benchmark (2000 random integers) ---")
    test_data = [random.randint(0, 10000) for _ in range(2000)]

    results = []
    for func, name in algorithms:
        _, elapsed, _ = benchmark(func, test_data, name)
        results.append((name, elapsed))

    results.sort(key=lambda x: x[1])
    for name, ms in results:
        bar = "█" * int(ms / 2)
        print(f"  {name:20s} {ms:8.2f} ms  {bar}")
