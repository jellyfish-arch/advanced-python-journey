"""
02_pytest_intro.py
------------------
Introduction to pytest, the most popular testing framework in the Python ecosystem.
Pytest allows for simpler syntax compared to unittest, using plain 'assert' statements.

Run this with: pytest testing/02_pytest_intro.py
(Note: Standard 'python' command won't run pytest automatically unless main is configured)
"""

import pytest

# Simple functions to test
def calculate_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return width * height

def format_name(first, last):
    return f"{first.capitalize()} {last.capitalize()}"

# Pytest doesn't require a class, just functions prefixed with 'test_'
def test_calculate_area_positive():
    assert calculate_area(10, 5) == 50
    assert calculate_area(0, 5) == 0

def test_format_name():
    assert format_name("john", "doe") == "John Doe"
    assert format_name("ALICE", "smith") == "Alice Smith"

# Testing for expected errors in pytest
def test_calculate_area_invalid_input():
    with pytest.raises(ValueError, match="Dimensions cannot be negative"):
        calculate_area(-1, 5)

if __name__ == "__main__":
    # In a professional project, you'd run 'pytest' from the terminal.
    # This block allows running it like a regular script for demonstration.
    print("Pytest discovery usually runs via terminal command: 'pytest testing/02_pytest_intro.py'")
    pytest.main([__file__])
