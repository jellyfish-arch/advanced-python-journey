"""
07 - Searching Algorithms
==========================
Implementations of Linear Search, Binary Search (iterative & recursive),
and Jump Search with performance comparison.

Key Concepts:
    - Linear Search — O(n)
    - Binary Search — O(log n), requires sorted input
    - Jump Search — O(√n), requires sorted input
    - Iterative vs recursive approaches
"""

import math
import time
import random


def linear_search(arr, target):
    """Linear Search — scans every element. O(n)."""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search_iterative(arr, target):
    """Binary Search (iterative) — halves search space each step. O(log n)."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    """Binary Search (recursive). O(log n)."""
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def jump_search(arr, target):
    """Jump Search — jumps √n steps then linear scan. O(√n)."""
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jump ahead until we pass the target
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search within the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1


def benchmark_search(func, data, target, name):
    """Time a search function and return the duration."""
    start = time.perf_counter()
    result = func(data, target)
    elapsed = (time.perf_counter() - start) * 1_000_000  # microseconds
    return name, elapsed, result


if __name__ == "__main__":
    # Small demo
    sample = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
    target = 23

    print("--- Searching Algorithms ---")
    print(f"Array:  {sample}")
    print(f"Target: {target}\n")

    print(f"  Linear Search:            index {linear_search(sample, target)}")
    print(f"  Binary Search (iterative): index {binary_search_iterative(sample, target)}")
    print(f"  Binary Search (recursive): index {binary_search_recursive(sample, target)}")
    print(f"  Jump Search:              index {jump_search(sample, target)}")

    # Not-found case
    print(f"\n  Search for 99: {linear_search(sample, 99)} (not found)")

    # Performance comparison on larger data
    print("\n--- Performance Benchmark (100,000 sorted elements) ---")
    large_data = sorted(random.sample(range(1_000_000), 100_000))
    search_target = large_data[75000]  # pick an element we know exists

    algorithms = [
        (linear_search, "Linear Search"),
        (binary_search_iterative, "Binary (Iterative)"),
        (binary_search_recursive, "Binary (Recursive)"),
        (jump_search, "Jump Search"),
    ]

    results = []
    for func, name in algorithms:
        _, elapsed, idx = benchmark_search(func, large_data, search_target, name)
        results.append((name, elapsed, idx))

    for name, us, idx in results:
        print(f"  {name:22s}  {us:10.2f} µs  (index: {idx})")
