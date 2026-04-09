# 08 - Iterators & Generators
# Intermediate Concept: Lazy evaluation, custom iterators, generator functions & expressions

import sys

# --- Built-in iterators ---
print("--- Built-in iteration protocol ---")
numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
# next(iterator) would raise StopIteration

print()

# --- Custom iterator class ---
class Countdown:
    """Iterator that counts down from a given number to 1."""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


print("--- Custom Iterator: Countdown ---")
for num in Countdown(5):
    print(f"  {num}...", end="")
print(" Liftoff! \n")


# --- Custom iterable: Fibonacci sequence ---
class FibonacciSequence:
    """Iterable that generates Fibonacci numbers up to a limit."""

    def __init__(self, max_value):
        self.max_value = max_value

    def __iter__(self):
        a, b = 0, 1
        while a <= self.max_value:
            yield a
            a, b = b, a + b


print("--- Fibonacci up to 100 ---")
fibs = list(FibonacciSequence(100))
print(f"  {fibs}\n")


# --- Generator function ---
def squares_generator(n):
    """Generate squares of numbers 1 to n lazily."""
    for i in range(1, n + 1):
        yield i ** 2


print("--- Generator: Squares ---")
gen = squares_generator(8)
print(f"  Type: {type(gen)}")
print(f"  Values: {list(gen)}")

print()

# --- Memory comparison: list vs generator ---
def memory_comparison():
    """Show memory difference between list and generator."""
    n = 1_000_000

    # List (stores all values in memory)
    big_list = [x ** 2 for x in range(n)]
    list_size = sys.getsizeof(big_list)

    # Generator (computes values on-the-fly)
    big_gen = (x ** 2 for x in range(n))
    gen_size = sys.getsizeof(big_gen)

    print("--- Memory Comparison (1M items) ---")
    print(f"  List size:      {list_size:>10,} bytes ({list_size / 1024 / 1024:.2f} MB)")
    print(f"  Generator size: {gen_size:>10,} bytes")
    print(f"  Ratio: List is {list_size / gen_size:.0f}x larger!")


memory_comparison()
print()

# --- Generator with send() ---
def running_average():
    """Generator that computes a running average."""
    total = 0
    count = 0
    average = None
    while True:
        value = yield average
        if value is not None:
            total += value
            count += 1
            average = total / count


print("--- Generator with send(): Running Average ---")
avg = running_average()
next(avg)  # Prime the generator
for score in [85, 90, 78, 92, 88]:
    result = avg.send(score)
    print(f"  Added {score} -> Running avg: {result:.2f}")

print()

# --- Generator pipeline (chaining) ---
def read_data(data):
    """Stage 1: Yield each item."""
    for item in data:
        yield item


def filter_valid(items):
    """Stage 2: Filter items with valid scores."""
    for item in items:
        if item.get("score") is not None and item["score"] >= 0:
            yield item


def normalize(items, max_score=100):
    """Stage 3: Normalize scores to 0-1 range."""
    for item in items:
        yield {
            "name": item["name"],
            "score": item["score"],
            "normalized": round(item["score"] / max_score, 2)
        }


def format_output(items):
    """Stage 4: Format for display."""
    for item in items:
        yield f"  {item['name']:<10} {item['score']:>3}/100  ->  {item['normalized']:.2f}"


# Raw data
raw_data = [
    {"name": "Arjun", "score": 87},
    {"name": "Priya", "score": None},
    {"name": "Ravi", "score": 92},
    {"name": "Sneha", "score": -1},
    {"name": "Kiran", "score": 76},
    {"name": "Meera", "score": 95},
]

# Build pipeline
pipeline = format_output(normalize(filter_valid(read_data(raw_data))))

print("--- Generator Pipeline: Data Processing ---")
for line in pipeline:
    print(line)

print()

# --- Generator expression vs list comprehension ---
print("--- Generator Expression ---")
gen_expr = (x ** 3 for x in range(1, 6))
print(f"  Generator: {gen_expr}")
print(f"  Sum of cubes (1-5): {sum(x ** 3 for x in range(1, 6))}")
print(f"  Max cube (1-10): {max(x ** 3 for x in range(1, 11))}")


# --- Main ---
if __name__ == "__main__":
    print("\n--- Summary ---")
    print("Covered: iterators, generators, send(), pipelines, memory efficiency")
    print("Key insight: Generators enable lazy evaluation and memory-efficient processing")
