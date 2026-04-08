# 06 - Magic (Dunder) Methods
# OOP Concept: __str__, __repr__, __len__, __add__, __eq__, __lt__, __getitem__, __contains__

class Vector:
    def __init__(self, *components):
        self.components = list(components)

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __str__(self):
        return f"<{', '.join(map(str, self.components))}>"

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions.")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(*result)

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions.")
        result = [a - b for a, b in zip(self.components, other.components)]
        return Vector(*result)

    def __mul__(self, scalar):
        return Vector(*[x * scalar for x in self.components])

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __eq__(self, other):
        return self.components == other.components

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __getitem__(self, index):
        return self.components[index]

    def __contains__(self, value):
        return value in self.components

    def __abs__(self):
        return self.magnitude()

    def magnitude(self):
        return sum(x ** 2 for x in self.components) ** 0.5

    def dot(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print(f"v1 = {v1}")
    print(f"v2 = repr: {repr(v2)}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v2 - v1 = {v2 - v1}")
    print(f"v1 * 3  = {v1 * 3}")
    print(f"2 * v2  = {2 * v2}")
    print(f"len(v1) = {len(v1)}")
    print(f"v1 == v1: {v1 == v1}")
    print(f"v1 < v2: {v1 < v2}")
    print(f"v1[0]: {v1[0]}")
    print(f"2 in v1: {2 in v1}")
    print(f"|v1| = {abs(v1):.4f}")
    print(f"v1 . v2 = {v1.dot(v2)}")
