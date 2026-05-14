from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

if __name__ == "__main__":
    factory = AnimalFactory()
    dog = factory.create_animal("dog")
    cat = factory.create_animal("cat")
    print(dog.speak())
    print(cat.speak())
