"""
08_edge_cases_validation.py
----------------------------
A practical example focused on testing complex validation logic.
Tests boundary conditions, invalid types, and unusual but valid scenarios.

Concepts:
- Boundary testing
- Data validation
- Comprehensive test coverage
"""

import pytest
import re

def validate_password(password):
    """
    Password Rules:
    - At least 8 characters
    - Contains at least one uppercase letter
    - Contains at least one digit
    - Contains at least one special character (!@#$%^&*)
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    
    if len(password) < 8:
        return False, "Too short"
    if not any(c.isupper() for c in password):
        return False, "Needs uppercase"
    if not any(c.isdigit() for c in password):
        return False, "Needs a digit"
    if not re.search(r"[!@#$%^&*]", password):
        return False, "Needs a special character"
    
    return True, "Valid"

# Tests for valid passwords - used this in Professional Testing section.
@pytest.mark.parametrize("pwd", [
    "StrongP@ss1",
    "Admin#2024",
    "very_Complex!9",
])
def test_valid_passwords(pwd):
    is_valid, message = validate_password(pwd)
    assert is_valid is True
    assert message == "Valid"

# Tests for invalid passwords (boundary cases)
@pytest.mark.parametrize("pwd, expected_msg", [
    ("Short1!", "Too short"),          # Exactly 7 chars
    ("nouppercase1!", "Needs uppercase"),
    ("NO_DIGITS!", "Needs a digit"),
    ("NoSpecialChar1", "Needs a special character"),
])
def test_invalid_passwords(pwd, expected_msg):
    is_valid, message = validate_password(pwd)
    assert is_valid is False
    assert message == expected_msg

# Test for incorrect type (Strict validation)
def test_validate_password_type_error():
    with pytest.raises(TypeError):
        validate_password(12345678)

if __name__ == "__main__":
    print("Running Edge Case & Validation Tests...")
    pytest.main([__file__])
