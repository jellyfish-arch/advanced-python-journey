# 02 - Lambda, Map, Filter, Reduce
# Intermediate Concept: Anonymous functions and functional programming tools

from functools import reduce

# --- Lambda basics ---
add = lambda a, b: a + b
print("Lambda add(3, 5):", add(3, 5))

square = lambda x: x ** 2
print("Lambda square(7):", square(7))

# --- map(): Apply a function to every element ---
temperatures_c = [0, 20, 37, 100, -40]
temperatures_f = list(map(lambda c: (c * 9/5) + 32, temperatures_c))
print("Celsius:   ", temperatures_c)
print("Fahrenheit:", temperatures_f)

# --- filter(): Keep elements that satisfy a condition ---
numbers = list(range(-10, 11))
positives = list(filter(lambda x: x > 0, numbers))
print("Positive numbers:", positives)

# --- Combining map and filter ---
# Get squares of even numbers from a list
raw = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, raw)))
print("Squares of evens:", even_squares)

# --- reduce(): Accumulate values into one result ---
nums = [1, 2, 3, 4, 5]
product = reduce(lambda acc, x: acc * x, nums)
print(f"Product of {nums}: {product}")

# Find the longest word using reduce
words = ["python", "is", "an", "incredibly", "powerful", "language"]
longest = reduce(lambda a, b: a if len(a) >= len(b) else b, words)
print(f"Longest word: '{longest}'")

# --- sorted() with lambda key ---
employees = [
    {"name": "Ananya", "salary": 75000, "experience": 3},
    {"name": "Vikram", "salary": 92000, "experience": 7},
    {"name": "Meera", "salary": 68000, "experience": 2},
    {"name": "Rahul", "salary": 85000, "experience": 5},
]

by_salary = sorted(employees, key=lambda e: e["salary"], reverse=True)
print("\nSorted by salary (desc):")
for emp in by_salary:
    print(f"  {emp['name']:>8} - Rs.{emp['salary']:,} ({emp['experience']} yrs)")

by_experience = sorted(employees, key=lambda e: e["experience"])
print("\nSorted by experience (asc):")
for emp in by_experience:
    print(f"  {emp['name']:>8} - {emp['experience']} years")

# --- Practical: Data pipeline using map + filter + reduce ---
transactions = [120.50, -45.00, 200.00, -30.75, 88.25, -15.00, 350.00]

# Step 1: Filter only credits (positive amounts)
credits = list(filter(lambda x: x > 0, transactions))
# Step 2: Apply 5% tax on each credit
taxed = list(map(lambda x: round(x * 0.95, 2), credits))
# Step 3: Sum up the total
total = reduce(lambda a, b: a + b, taxed)

print(f"\nCredits: {credits}")
print(f"After 5% tax: {taxed}")
print(f"Total income after tax: Rs.{total:,.2f}")


# --- Main ---
if __name__ == "__main__":
    print("\n--- Summary ---")
    print("Demonstrated: lambda, map(), filter(), reduce(), sorted()")
    print("Practical pipeline: filter -> map -> reduce")
