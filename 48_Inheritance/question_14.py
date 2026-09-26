# Question:
# Simulate abstract methods: base class raises NotImplementedError,
# child class must implement it.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")

    def describe(self):
        return f"Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"

import math

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r**2
    def perimeter(self):
        return 2 * math.pi * self.r

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2
    def perimeter(self):
        return 4 * self.side

c = Circle(5)
sq = Square(4)

print(f"Circle: {c.describe()}")
print(f"Square: {sq.describe()}")

# Calling on base class raises error
try:
    s = Shape()
    s.area()
except NotImplementedError as e:
    print(f"\nBase Shape.area() raises: {e}")
