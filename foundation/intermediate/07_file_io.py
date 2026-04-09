# 07 - File I/O Operations
# Intermediate Concept: Reading, writing, and processing files with context managers

import os
import json
import csv
from pathlib import Path

# --- Writing to a text file ---
def write_text_file(filepath, lines):
    """Write a list of lines to a text file."""
    with open(filepath, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"[OK] Written {len(lines)} lines to '{filepath}'")


# --- Reading a text file ---
def read_text_file(filepath):
    """Read and display contents of a text file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"[DOC] Contents of '{filepath}':")
    print(content)
    return content


# --- Appending to a file ---
def append_to_file(filepath, text):
    """Append text to an existing file."""
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"[+] Appended to '{filepath}'")


# Create a sample text file
sample_dir = Path(__file__).parent / "_sample_output"
sample_dir.mkdir(exist_ok=True)

notes = [
    "Python Intermediate Notes",
    "=========================",
    "1. List comprehensions are concise and powerful.",
    "2. Decorators modify function behavior elegantly.",
    "3. Error handling makes code robust and reliable.",
    "4. File I/O is essential for data processing.",
    "5. Always use context managers (with statement) for files.",
]

txt_path = sample_dir / "notes.txt"
write_text_file(txt_path, notes)
append_to_file(txt_path, "6. Practice makes perfect!")
read_text_file(txt_path)

# --- Line-by-line reading (memory efficient for large files) ---
print("--- Line-by-line reading ---")
with open(txt_path, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        if line.strip():  # Skip empty lines
            print(f"  Line {line_num:>2}: {line.rstrip()}")

print()

# --- Working with JSON files ---
student_data = {
    "students": [
        {"name": "Arjun", "age": 22, "courses": ["Python", "ML"], "gpa": 8.7},
        {"name": "Priya", "age": 21, "courses": ["Python", "Web Dev"], "gpa": 9.1},
        {"name": "Ravi", "age": 23, "courses": ["DSA", "Python"], "gpa": 7.8},
    ],
    "department": "Computer Science",
    "year": 2026,
}

json_path = sample_dir / "students.json"

# Write JSON
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(student_data, f, indent=2, ensure_ascii=False)
print(f"[OK] Written JSON to '{json_path}'")

# Read JSON
with open(json_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"\n[DOC] Students in {loaded['department']} ({loaded['year']}):")
for student in loaded["students"]:
    courses = ", ".join(student["courses"])
    print(f"  {student['name']:>8} | GPA: {student['gpa']} | Courses: {courses}")

print()

# --- Working with CSV files ---
csv_path = sample_dir / "employees.csv"

employees = [
    {"name": "Ananya", "department": "Engineering", "salary": 85000},
    {"name": "Vikram", "department": "Design", "salary": 72000},
    {"name": "Meera", "department": "Engineering", "salary": 91000},
    {"name": "Rahul", "department": "Marketing", "salary": 68000},
    {"name": "Sneha", "department": "Engineering", "salary": 95000},
]

# Write CSV
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "department", "salary"])
    writer.writeheader()
    writer.writerows(employees)
print(f"[OK] Written CSV to '{csv_path}'")

# Read CSV
with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("\n[DOC] Employee Data:")
    print(f"  {'Name':<10} {'Department':<15} {'Salary':>10}")
    print(f"  {'-'*10} {'-'*15} {'-'*10}")
    for row in reader:
        print(f"  {row['name']:<10} {row['department']:<15} Rs.{int(row['salary']):>8,}")

print()

# --- File metadata using pathlib ---
print("--- File Information ---")
for filepath in sample_dir.iterdir():
    stat = filepath.stat()
    size_kb = stat.st_size / 1024
    print(f"  {filepath.name:<20} {size_kb:>6.2f} KB  ({filepath.suffix})")


# --- Cleanup (optional) ---
def cleanup(directory):
    """Remove sample output files."""
    for file in directory.iterdir():
        file.unlink()
    directory.rmdir()
    print(f"\n[CLEAN] Cleaned up '{directory}'")


# Uncomment to clean up:
# cleanup(sample_dir)


# --- Main ---
if __name__ == "__main__":
    print("\n--- Summary ---")
    print("Covered: text files, JSON, CSV, pathlib, context managers")
    print(f"Output directory: {sample_dir}")
