# 05 - Abstraction
# OOP Concept: Abstract Base Classes (ABC), abstract methods, hiding internal complexity

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    def __init__(self, currency="USD"):
        self.currency = currency

    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, transaction_id, amount):
        pass

    # Concrete method shared by all
    def format_amount(self, amount):
        return f"{self.currency} {amount:.2f}"

    def validate(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")


class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.validate(amount)
        txn_id = f"STR-{id(self) % 10000}"
        print(
            f"[Stripe] Processing {self.format_amount(amount)} -> TXN: {txn_id}")
        return txn_id

    def refund(self, transaction_id, amount):
        self.validate(amount)
        print(
            f"[Stripe] Refunding {self.format_amount(amount)} for TXN: {transaction_id}")


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.validate(amount)
        txn_id = f"PPL-{id(self) % 10000}"
        print(
            f"[PayPal] Processing {self.format_amount(amount)} -> TXN: {txn_id}")
        return txn_id

    def refund(self, transaction_id, amount):
        self.validate(amount)
        print(
            f"[PayPal] Refunding {self.format_amount(amount)} for TXN: {transaction_id}")


class CryptoProcessor(PaymentProcessor):
    def __init__(self, coin="BTC"):
        super().__init__(currency=coin)

    def process_payment(self, amount):
        self.validate(amount)
        txn_id = f"CRY-{id(self) % 10000}"
        print(
            f"[Crypto/{self.currency}] Processing {amount} coins -> TXN: {txn_id}")
        return txn_id

    def refund(self, transaction_id, amount):
        print(f"[Crypto] Refunds are not supported for TXN: {transaction_id}")


if __name__ == "__main__":
    # Cannot instantiate abstract class
    try:
        p = PaymentProcessor()
    except TypeError as e:
        print(f"Error: {e}\n")

    processors = [StripeProcessor(), PayPalProcessor(), CryptoProcessor("ETH")]

    for proc in processors:
        txn = proc.process_payment(99.99)
        proc.refund(txn, 99.99)
        print()
