# Question:
# Create a Circle class with private __radius.
# Property radius with validation (must be > 0).
# Computed area and circumference as read-only properties.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Uses setter

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be numeric.")
        if value <= 0:
            raise ValueError(f"Radius must be > 0, got {value}")
        self.__radius = value

    @property
    def area(self):
        return math.pi * self.__radius ** 2

    @property
    def circumference(self):
        return 2 * math.pi * self.__radius

    def __str__(self):
        return (f"Circle(radius={self.__radius}, "
                f"area={self.area:.4f}, circumference={self.circumference:.4f})")

c = Circle(5)
print(c)

c.radius = 10
print(c)

try:
    c.radius = -3
except ValueError as e:
    print(f"Error: {e}")

try:
    c.radius = 0
except ValueError as e:
    print(f"Error: {e}")
