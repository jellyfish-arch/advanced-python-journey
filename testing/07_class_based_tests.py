"""
07_class_based_tests.py
------------------------
Demonstrates how to organize related tests into classes. 
This is useful for sharing setup/teardown logic across multiple test cases.

Concepts:
- setup_method and teardown_method in Pytest
- setUp and tearDown in Unittest
- Logical grouping of tests
"""

import unittest
import pytest

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

# --- Pytest Class Example ---
class TestBankAccountPytest:
    def setup_method(self, method):
        """Runs before every test method."""
        print(f"\nSetting up for: {method.__name__}")
        self.account = BankAccount(100)

    def teardown_method(self, method):
        """Runs after every test method."""
        print(f"Tearing down after: {method.__name__}")

    def test_initial_balance(self):
        assert self.account.balance == 100

    def test_deposit(self):
        self.account.deposit(50)
        assert self.account.balance == 150

    def test_withdraw_success(self):
        self.account.withdraw(40)
        assert self.account.balance == 60

# --- Unittest Class Example ---
class TestBankAccountUnittest(unittest.TestCase):
    def setUp(self):
        """Built-in unittest setup."""
        self.account = BankAccount(200)

    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(300)

if __name__ == "__main__":
    print("Running Class-Based Tests...")
    pytest.main([__file__, "-s"])
