"""
06_testing_exceptions.py
-------------------------
Testing that your code fails correctly is just as important as testing that it works.
This handles edge cases where invalid input should trigger exceptions.

Concepts:
- self.assertRaises (unittest)
- pytest.raises (pytest)
"""

import unittest
import pytest

# Logic to test - used this in Professional Testing section.
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return a / b

# --- Unittest Approach ---
class TestUnittestExceptions(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Denominator cannot be zero")

# --- Pytest Approach ---
def test_pytest_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide(10, 0)
    assert "Denominator cannot be zero" in str(exc_info.value)

if __name__ == "__main__":
    print("Running Exception Tests (Unittest followed by Pytest)...")
    # Running unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUnittestExceptions)
    unittest.TextTestRunner().run(suite)
    
    # Running pytest
    pytest.main([__file__])
