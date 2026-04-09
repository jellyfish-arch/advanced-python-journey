# 01 - List Comprehensions
# Intermediate Concept: Creating lists concisely with comprehensions, nested loops, and conditions

# --- Basic list comprehension ---
squares = [x ** 2 for x in range(1, 11)]
print("Squares 1-10:", squares)

# --- With condition (filtering) ---
even_squares = [x ** 2 for x in range(1, 21) if x % 2 == 0]
print("Even squares:", even_squares)

# --- String manipulation ---
words = ["hello", "world", "python", "is", "awesome"]
capitalized = [word.upper() for word in words if len(word) > 3]
print("Capitalized (len > 3):", capitalized)

# --- Nested comprehension (flatten a matrix) ---
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flat = [num for row in matrix for num in row]
print("Flattened matrix:", flat)

# --- Transpose a matrix ---
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transposed matrix:", transposed)

# --- Dictionary comprehension ---
names = ["alice", "bob", "charlie", "diana"]
name_lengths = {name: len(name) for name in names}
print("Name lengths:", name_lengths)

# --- Set comprehension (unique first letters) ---
sentences = "the quick brown fox jumps over the lazy dog"
unique_first_letters = {word[0] for word in sentences.split()}
print("Unique first letters:", sorted(unique_first_letters))

# --- Conditional expression in comprehension ---
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 11)]
print("Even/Odd labels:", labels)

# --- Practical: Filtering and transforming data ---
students = [
    {"name": "Arjun", "score": 87},
    {"name": "Priya", "score": 45},
    {"name": "Ravi", "score": 92},
    {"name": "Sneha", "score": 38},
    {"name": "Kiran", "score": 76},
]

passed = [s["name"] for s in students if s["score"] >= 50]
print("Passed students:", passed)

grade_map = {
    s["name"]: ("Distinction" if s["score"] >= 85 else
                "Pass" if s["score"] >= 50 else
                "Fail")
    for s in students
}
print("Grade map:", grade_map)


# --- Main ---
if __name__ == "__main__":
    print("\n--- Summary ---")
    print(f"Total squares generated: {len(squares)}")
    print(f"Matrix dimensions: {len(matrix)}x{len(matrix[0])}")
    print(f"Students processed: {len(students)}")
