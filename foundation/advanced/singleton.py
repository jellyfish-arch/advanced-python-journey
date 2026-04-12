class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating instance")
            cls._instance = super().__new__(cls)
        return cls._instance


a = Singleton()
b = Singleton()

print(a is b)  # True
