# 10 - Design Patterns: Singleton + Factory
# OOP Concept: Singleton (one instance), Factory Method (object creation abstraction)

# ─── SINGLETON PATTERN ─────────────────────────────────────────────────────────

class DatabaseConnection:
    """
    Singleton: Only one DB connection instance exists at a time.
    """
    _instance = None

    def __new__(cls, host="localhost", port=5432, db="mydb"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.host = host
            cls._instance.port = port
            cls._instance.db = db
            cls._instance.connected = False
            print(f"[Singleton] New DB connection created: {host}:{port}/{db}")
        return cls._instance

    def connect(self):
        if not self.connected:
            self.connected = True
            print(f"[DB] Connected to {self.host}:{self.port}/{self.db}")
        else:
            print("[DB] Already connected.")

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Not connected to database.")
        print(f"[DB] Executing: {sql}")

    def disconnect(self):
        self.connected = False
        print("[DB] Disconnected.")


# ─── FACTORY PATTERN ────────────────────────────────────────────────────────────

class Notification:
    def send(self, recipient, message):
        raise NotImplementedError


class EmailNotification(Notification):
    def send(self, recipient, message):
        print(f"[Email] To: {recipient} | {message}")


class SMSNotification(Notification):
    def send(self, recipient, message):
        print(f"[SMS] To: {recipient} | {message}")


class PushNotification(Notification):
    def send(self, recipient, message):
        print(f"[Push] To: {recipient} | {message}")


class NotificationFactory:
    """
    Factory: Creates the correct Notification object based on type string.
    Decouples object creation from usage.
    """
    _registry = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification,
    }

    @classmethod
    def create(cls, notification_type: str) -> Notification:
        key = notification_type.lower()
        if key not in cls._registry:
            raise ValueError(f"Unknown notification type: '{notification_type}'. "
                             f"Valid: {list(cls._registry.keys())}")
        return cls._registry[key]()

    @classmethod
    def register(cls, name, notification_class):
        """Extend factory with new types at runtime."""
        cls._registry[name.lower()] = notification_class
        print(f"[Factory] Registered new type: '{name}'")


# ─── Main ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Singleton ===")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection("remotehost", 3306, "prod")  # Same instance
    print(f"Same instance: {db1 is db2}")

    db1.connect()
    db2.connect()  # Already connected
    db1.query("SELECT * FROM users;")
    db1.disconnect()

    print("\n=== Factory ===")
    for ntype in ["email", "sms", "push"]:
        notif = NotificationFactory.create(ntype)
        notif.send("jellyfish@example.com", "Your OTP is 4821")

    try:
        NotificationFactory.create("telegram")
    except ValueError as e:
        print(f"Error: {e}")

    # Register a new type at runtime
    class SlackNotification(Notification):
        def send(self, recipient, message):
            print(f"[Slack] To: #{recipient} | {message}")

    NotificationFactory.register("slack", SlackNotification)
    NotificationFactory.create("slack").send(
        "dev-channel", "Deployment successful!")
