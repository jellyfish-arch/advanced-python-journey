"""
01_unittest_basics.py
---------------------
An introduction to Python's built-in 'unittest' module.
This script demonstrates how to create a test case, use common assertions,
and run tests using the standard library.

Concepts:
- unittest.TestCase
- Assertions: assertEqual, assertTrue, assertFalse
- Running tests with unittest.main()
"""

import unittest

# 1. The code we want to test (usually in a separate file) - it can be in the same file for simplicity.
def add_numbers(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def greet(name):
    if not name:
        return "Hello, Stranger!"
    return f"Hello, {name}!"

# 2. Creating the Test Class
class TestBasics(unittest.TestCase):
    
    def test_add_numbers(self):
        """Test simple addition logic."""
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_is_even(self):
        """Test boolean logic for even numbers."""
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(-1))

    def test_greet(self):
        """Test string return values and conditional logic."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet(""), "Hello, Stranger!")
        self.assertEqual(greet(None), "Hello, Stranger!")

# 3. Execution Block
if __name__ == "__main__":
    print("Running Unittest Basics...")
    # This invokes the unittest runner
    unittest.main()
