# 01 - Classes and Objects
# OOP Concept: Defining classes, creating objects, using __init__ and instance methods

class Car:
    # Class variable (shared across all instances)
    total_cars = 0

    def __init__(self, brand, model, year):
        # Instance variables (unique to each object)
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
        Car.total_cars += 1

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} started.")
        else:
            print(f"{self.brand} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} stopped.")
        else:
            print(f"{self.brand} {self.model} is already stopped.")

    def get_info(self):
        status = "Running" if self.is_running else "Stopped"
        return f"{self.year} {self.brand} {self.model} [{status}]"

    @classmethod
    def get_total_cars(cls):
        return f"Total cars created: {cls.total_cars}"


# --- Main ---
if __name__ == "__main__":
    car1 = Car("Toyota", "Supra", 2023)
    car2 = Car("Nissan", "GT-R", 2022)

    print(car1.get_info())
    car1.start()
    car1.start()  # Already running
    car1.stop()

    print(car2.get_info())
    print(Car.get_total_cars())
