# Question:
# Single inheritance: Create class Shape with an area() method that returns 0.
# Create class Circle inheriting from Shape, override area() to compute circle area.

import math

class Shape:
    def area(self):
        return 0

    def __str__(self):
        return f"Shape with area={self.area():.4f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius}, area={self.area():.4f})"

s = Shape()
c = Circle(7)

print(s)
print(c)
print(f"Circle inherits from Shape: {isinstance(c, Shape)}")
