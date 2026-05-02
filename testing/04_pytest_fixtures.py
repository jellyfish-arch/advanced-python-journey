"""
04_pytest_fixtures.py
----------------------
Fixtures are functions that run before (and optionally after) your tests.
They provide a fixed baseline so that tests can be reliably repeated.

Concepts:
- Setup and Teardown
- Reusable state
- Decoupling data preparation from logic
"""

import pytest
import os

# 1. A fixture to provide a temporary "database" (a simple list in this example)
@pytest.fixture
def sample_user_db():
    """Initializes a mock user database for tests."""
    print("\n[Setup] Creating temporary user database...")
    db = {
        1: {"username": "alice", "email": "alice@example.com"},
        2: {"username": "bob", "email": "bob@example.com"}
    }
    return db

# 2. A fixture with 'yield' for setup and teardown - used this in Professional Testing section.
@pytest.fixture
def temp_file():
    """Creates a temporary file and deletes it after the test."""
    filename = "test_temp_file.txt"
    with open(filename, "w") as f:
        f.write("Temporary Data")
    
    print(f"\n[Setup] Created {filename}")
    yield filename  # The test runs here
    
    # Teardown logic
    if os.path.exists(filename):
        os.remove(filename)
        print(f"[Teardown] Deleted {filename}")

# --- Tests utilizing the fixtures ---

def test_user_exists(sample_user_db):
    """The sample_user_db fixture is injected automatically."""
    assert sample_user_db[1]["username"] == "alice"

def test_temp_file_creation(temp_file):
    """Verifies that the file exists during the test run."""
    assert os.path.exists(temp_file)
    with open(temp_file, "r") as f:
        assert f.read() == "Temporary Data"

if __name__ == "__main__":
    # Use -s to see print statements in output
    pytest.main([__file__, "-s"])
