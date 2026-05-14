import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.model = "Basic Model"
        self.color = "Red"
        self.options = "None"

    def __str__(self):
        return f"{self.color} {self.model} with {self.options}"

if __name__ == "__main__":
    car = Car()
    prototype = Prototype()
    prototype.register_object("basic_car", car)
    
    cloned_car = prototype.clone("basic_car", color="Blue")
    print("Original:", car)
    print("Cloned:", cloned_car)
