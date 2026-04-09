# 06 - String Formatting & Manipulation
# Intermediate Concept: f-strings, format(), template patterns, regex basics

import re
from string import Template

# --- f-string formatting ---
name = "Arjun"
balance = 154832.5
pi = 3.14159265

print(f"Name: {name!r}")                    # repr
print(f"Balance: Rs.{balance:>15,.2f}")       # right-aligned, comma-separated
print(f"Pi: {pi:.4f}")                       # 4 decimal places
print(f"Binary of 42: {42:08b}")             # binary with zero-padding
print(f"Hex of 255: {255:#06x}")             # hex with prefix

print()

# --- Alignment and padding ---
products = [
    ("Laptop", 79999),
    ("Mouse", 599),
    ("Keyboard", 2499),
    ("Monitor", 24999),
    ("USB Cable", 199),
]

print(f"{'Product':<15} {'Price':>10}")
print("-" * 27)
for product, price in products:
    print(f"{product:<15} Rs.{price:>8,}")

print()

# --- str.format() method ---
template = "Hello {name}, you have {count} unread messages."
print(template.format(name="Priya", count=42))

# Indexed and reused
print("{0} vs {1}: {0} wins!".format("Python", "Java"))

print()

# --- String Template (safe substitution) ---
email_template = Template(
    "Dear $name,\n"
    "Your order #$order_id has been $status.\n"
    "Expected delivery: $date\n"
)

print(email_template.substitute(
    name="Vikram",
    order_id="ORD-2026-4521",
    status="shipped",
    date="12 Apr 2026"
))

# safe_substitute won't raise error for missing keys
partial = Template("Hi $name, your role is $role")
print(partial.safe_substitute(name="Sneha"))  # $role stays as-is

print()

# --- Useful string methods ---
text = "  Hello, World! Welcome to Python Programming.  "

print(f"Strip:    '{text.strip()}'")
print(f"Title:    '{text.strip().title()}'")
print(f"Swapcase: '{text.strip().swapcase()}'")
print(f"Center:   '{name.center(20, '-')}'")
print(f"Zfill:    '{'42'.zfill(8)}'")

# Splitting and joining
csv_line = "Arjun,25,Bangalore,Developer"
fields = csv_line.split(",")
print(f"\nCSV Split: {fields}")
print(f"Rejoined:  {' | '.join(fields)}")

# Checking content
print(f"\n'Python3'.isalnum(): {'Python3'.isalnum()}")
print(f"'12345'.isdigit(): {'12345'.isdigit()}")
print(f"'hello'.isalpha(): {'hello'.isalpha()}")

print()

# --- Regular expressions (basics) ---
text = "Contact us at support@example.com or sales@company.co.in for queries."

# Find all email addresses
emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', text)
print(f"Emails found: {emails}")

# Extract phone numbers
phone_text = "Call us at +91-9876543210 or 080-12345678 for support."
phones = re.findall(r'[\+\d][\d-]{9,}', phone_text)
print(f"Phones found: {phones}")

# Replace pattern
messy = "This   has    too     many    spaces"
clean = re.sub(r'\s+', ' ', messy)
print(f"Cleaned: '{clean}'")

# Validate format
def is_valid_email(email):
    pattern = r'^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

test_emails = ["user@example.com", "invalid@", "test.user@domain.co.in"]
for email in test_emails:
    status = "[OK] Valid" if is_valid_email(email) else "[X] Invalid"
    print(f"  {email:30} {status}")


# --- Main ---
if __name__ == "__main__":
    print("\n--- Summary ---")
    print("Covered: f-strings, str.format(), Template, string methods, regex")
