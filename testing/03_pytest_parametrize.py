"""
03_pytest_parametrize.py
-------------------------
Demonstrates how to clean up redundant test code using @pytest.mark.parametrize.
This allows running the same test logic with multiple sets of data.

Concepts:
- Reducing boilerplate
- Data-driven testing
"""

import pytest

def is_palindrome(s):
    if not isinstance(s, str):
        return False
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

# Instead of writing 5 different test functions, we use parametrization
@pytest.mark.parametrize("input_str, expected", [
    ("radar", True),
    ("Python", False),
    ("A man, a plan, a canal: Panama", True),
    ("", True),
    ("12321", True),
    (123, False),  # Testing non-string input
])
def test_palindrome(input_str, expected):
    """A single test function that runs multiple scenarios."""
    assert is_palindrome(input_str) == expected

if __name__ == "__main__":
    print("Running Parametrized Tests...")
    pytest.main([__file__])
