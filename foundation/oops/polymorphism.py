# 03 - Polymorphism
# OOP Concept: Same interface, different behavior (method overriding + duck typing)

import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter()")

    def describe(self):
        return (f"{self.__class__.__name__} -> "
                f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# Duck typing: any object with area() works
class CustomHexagon:
    def __init__(self, side):
        self.side = side

    def area(self):
        return (3 * math.sqrt(3) / 2) * self.side ** 2

    def perimeter(self):
        return 6 * self.side


def print_shape_info(shape):
    # Works on any object with area() and perimeter()
    print(shape.describe() if hasattr(shape, "describe") else
          f"{shape.__class__.__name__} -> Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")


if __name__ == "__main__":
    shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5), CustomHexagon(4)]

    for shape in shapes:
        print_shape_info(shape)
