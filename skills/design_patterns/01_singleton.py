class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def connect(self):
        print("Connected to the database.")

if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    assert id(db1) == id(db2)
    print("Singleton pattern works.")
