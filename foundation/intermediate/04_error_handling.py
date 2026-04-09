# 04 - Error Handling
# Intermediate Concept: try/except/else/finally, custom exceptions, best practices

import json

# --- Basic try/except ---
def safe_divide(a, b):
    """Divide two numbers with error handling."""
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"[ERROR] Cannot divide {a} by zero!")
        return None
    except TypeError as e:
        print(f"[ERROR] Invalid types: {e}")
        return None
    else:
        # Runs only if no exception was raised
        print(f"[OK] {a} / {b} = {result:.4f}")
        return result
    finally:
        # Always runs, regardless of exception
        print(f"   (Division attempt complete for {a}, {b})")


safe_divide(10, 3)
safe_divide(10, 0)
safe_divide("10", [])

print()

# --- Multiple exception types ---
def parse_data(raw_input):
    """Parse a JSON string and extract a value safely."""
    try:
        data = json.loads(raw_input)
        value = data["score"]
        normalized = value / 100
    except json.JSONDecodeError:
        print("[ERROR] Invalid JSON format")
        return None
    except KeyError:
        print("[ERROR] Missing 'score' key in data")
        return None
    except (TypeError, ZeroDivisionError) as e:
        print(f"[ERROR] Processing error: {e}")
        return None
    else:
        print(f"[OK] Parsed score: {value}, Normalized: {normalized:.2f}")
        return normalized


parse_data('{"score": 85}')
parse_data('invalid json')
parse_data('{"name": "test"}')

print()

# --- Custom exceptions ---
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        super().__init__(
            f"Cannot withdraw Rs.{amount:,.2f} from balance Rs.{balance:,.2f}. "
            f"Short by Rs.{self.deficit:,.2f}"
        )


class InvalidAmountError(Exception):
    """Raised when transaction amount is invalid."""
    pass


class BankAccount:
    """Simple bank account with custom exception handling."""

    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Deposit amount must be positive, got Rs.{amount}")
        self.balance += amount
        self.transactions.append(f"+Rs.{amount:,.2f}")
        print(f"[+] Deposited Rs.{amount:,.2f}. Balance: Rs.{self.balance:,.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Withdrawal amount must be positive, got Rs.{amount}")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        self.transactions.append(f"-Rs.{amount:,.2f}")
        print(f"[-] Withdrew Rs.{amount:,.2f}. Balance: Rs.{self.balance:,.2f}")

    def statement(self):
        print(f"\n--- Statement for {self.holder} ---")
        print(f"   Balance: Rs.{self.balance:,.2f}")
        print(f"   Transactions: {' | '.join(self.transactions)}")


# Using custom exceptions
account = BankAccount("Vikram", balance=5000)

try:
    account.deposit(3000)
    account.withdraw(2000)
    account.withdraw(10000)  # Should fail
except InsufficientFundsError as e:
    print(f"[BLOCKED] {e}")
except InvalidAmountError as e:
    print(f"[BLOCKED] {e}")

account.statement()

print()

# --- Exception chaining (raise from) ---
def load_config(filepath):
    """Load configuration from a file with exception chaining."""
    try:
        with open(filepath, "r") as f:
            config = json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError(f"Config file '{filepath}' is missing") from e
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Config file '{filepath}' has invalid JSON") from e
    return config


try:
    config = load_config("nonexistent_config.json")
except RuntimeError as e:
    print(f"[WARN] {e}")
    print(f"   Caused by: {e.__cause__}")

print()

# --- Context-based cleanup pattern ---
def process_records(records):
    """Process records with per-item error handling."""
    successful = 0
    failed = 0
    errors = []

    for i, record in enumerate(records):
        try:
            name = record["name"]
            score = int(record["score"])
            if score < 0 or score > 100:
                raise ValueError(f"Score {score} out of range (0-100)")
            print(f"  [OK] {name}: {score}/100")
            successful += 1
        except (KeyError, ValueError, TypeError) as e:
            failed += 1
            errors.append(f"Record {i}: {e}")
            print(f"  [FAIL] Record {i} failed: {e}")

    print(f"\nProcessed: {successful} success, {failed} failed")
    if errors:
        print("Errors:", errors)


records = [
    {"name": "Alice", "score": "92"},
    {"name": "Bob", "score": "invalid"},
    {"name": "Charlie", "score": "78"},
    {"score": "65"},           # Missing name
    {"name": "Eve", "score": "150"},  # Out of range
]

print("--- Processing Records ---")
process_records(records)


# --- Main ---
if __name__ == "__main__":
    print("\n--- Summary ---")
    print("Covered: try/except/else/finally, custom exceptions,")
    print("         exception chaining, per-item error handling")
