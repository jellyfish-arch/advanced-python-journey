# 09 - Decorators and Properties
# OOP Concept: @property, @setter, @deleter, custom class decorators

def readonly(func):
    """Custom decorator: marks a method as read-only (documentation + enforcement)."""
    func._readonly = True

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.__doc__ = f"[READ-ONLY] {func.__doc__ or func.__name__}"
    return wrapper


def validate_positive(attr_name):
    """Decorator factory: validates that a value is positive before setting."""
    def decorator(func):
        def wrapper(self, value):
            if value < 0:
                raise ValueError(
                    f"{attr_name} cannot be negative. Got: {value}")
            return func(self, value)
        return wrapper
    return decorator


class Temperature:
    def __init__(self, celsius=0.0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius

    @celsius.setter
    @validate_positive("Celsius")
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9

    @property
    def kelvin(self):
        return self._celsius + 273.15

    @readonly
    def description(self):
        if self._celsius < 0:
            return "Freezing"
        elif self._celsius < 20:
            return "Cold"
        elif self._celsius < 35:
            return "Warm"
        return "Hot"

    def __str__(self):
        return (f"{self._celsius:.2f}°C | "
                f"{self.fahrenheit:.2f}°F | "
                f"{self.kelvin:.2f}K")


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2


if __name__ == "__main__":
    t = Temperature(25)
    print(f"Temp: {t}")
    print(f"Description: {t.description()}")

    t.fahrenheit = 32
    print(f"After setting 32°F: {t}")

    try:
        t.celsius = -10
    except ValueError as e:
        print(f"Error: {e}")

    print()

    c = Circle(5)
    print(f"Radius: {c.radius}, Diameter: {c.diameter}, Area: {c.area:.4f}")
    c.radius = 10
    print(f"Updated Area: {c.area:.4f}")

    del c.radius
