# 04 - Encapsulation
# OOP Concept: Public, protected (_), private (__) attributes + getters/setters + @property

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner             # public
        self._account_type = "Savings"  # protected (convention)
        self.__balance = balance       # private (name-mangled)
        self.__transaction_log = []

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        raise AttributeError(
            "Direct balance assignment not allowed. Use deposit/withdraw.")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        self.__log(f"Deposited: +{amount}")
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        self.__log(f"Withdrew: -{amount}")
        return self.__balance

    def get_statement(self):
        print(f"\n--- Statement for {self.owner} ({self._account_type}) ---")
        for entry in self.__transaction_log:
            print(f"  {entry}")
        print(f"  Current Balance: {self.__balance}")

    def __log(self, message):
        self.__transaction_log.append(message)


if __name__ == "__main__":
    acc = BankAccount("Jellyfish", 1000)

    acc.deposit(500)
    acc.withdraw(200)
    acc.deposit(150)

    try:
        acc.withdraw(5000)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        acc.balance = 9999  # Should raise
    except AttributeError as e:
        print(f"Error: {e}")

    print(f"Balance via property: {acc.balance}")
    acc.get_statement()

    # Private name mangling (accessed externally like this, bad practice)
    # print(acc._BankAccount__balance)  # Works but shouldn't be used
