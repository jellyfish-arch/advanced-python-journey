# 08 - Multiple Inheritance & Mixins
# OOP Concept: Multiple inheritance, MRO (Method Resolution Order), Mixin pattern

class LogMixin:
    """Mixin to add logging capability to any class."""

    def log(self, message):
        print(f"[LOG | {self.__class__.__name__}] {message}")


class SerializeMixin:
    """Mixin to add dict/string serialization."""

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    def to_string(self):
        return ", ".join(f"{k}={v}" for k, v in self.to_dict().items())


class TimestampMixin:
    """Mixin to track creation time."""
    from datetime import datetime

    def created_at(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class BaseModel:
    def __init__(self, model_id):
        self.model_id = model_id

    def identify(self):
        return f"Model ID: {self.model_id}"


# Multiple inheritance: BaseModel + all three Mixins
class UserProfile(LogMixin, SerializeMixin, TimestampMixin, BaseModel):
    def __init__(self, model_id, username, email, role="user"):
        super().__init__(model_id)
        self.username = username
        self.email = email
        self.role = role

    def promote(self, new_role):
        self.log(f"Promoting {self.username} from {self.role} to {new_role}")
        self.role = new_role


class Product(LogMixin, SerializeMixin, BaseModel):
    def __init__(self, model_id, name, price, stock):
        super().__init__(model_id)
        self.name = name
        self.price = price
        self.stock = stock

    def restock(self, qty):
        self.stock += qty
        self.log(f"Restocked {self.name} by {qty}. Total: {self.stock}")


if __name__ == "__main__":
    user = UserProfile("U-001", "jellyfish_arch", "jelly@example.com")
    print(user.identify())
    print(user.to_string())
    user.promote("admin")
    print(f"Created at: {user.created_at()}\n")

    product = Product("P-042", "Mechanical Keyboard", 129.99, 50)
    print(product.to_dict())
    product.restock(20)

    # MRO shows resolution order
    print(f"\nMRO for UserProfile:")
    for cls in UserProfile.__mro__:
        print(f"  {cls}")
