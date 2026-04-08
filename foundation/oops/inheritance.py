# 02 - Inheritance
# OOP Concept: Single & multilevel inheritance, method overriding, super()

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} makes a sound."

    def describe(self):
        return f"{self.name} is a {self.species}."


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self):
        return f"{self.name} says: Woof!"

    def fetch(self):
        return f"{self.name} fetches the ball!"


class ServiceDog(Dog):
    def __init__(self, name, breed, role):
        super().__init__(name, breed)
        self.role = role

    def speak(self):
        return f"{self.name} (Service Dog) says: Woof! I'm on duty."

    def perform_duty(self):
        return f"{self.name} is performing: {self.role}"


class Cat(Animal):
    def __init__(self, name, indoor):
        super().__init__(name, species="Cat")
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says: Meow!"

    def status(self):
        return "Indoor cat" if self.indoor else "Outdoor cat"


if __name__ == "__main__":
    dog = Dog("Rex", "Labrador")
    print(dog.describe())
    print(dog.speak())
    print(dog.fetch())

    print()

    service = ServiceDog("Buddy", "German Shepherd",
                         "Guiding the visually impaired")
    print(service.speak())
    print(service.perform_duty())

    print()

    cat = Cat("Nyx", indoor=True)
    print(cat.describe())
    print(cat.speak())
    print(cat.status())

    print()
    print(isinstance(service, Dog))       # True
    print(isinstance(service, Animal))    # True
    print(isinstance(dog, ServiceDog))    # False
