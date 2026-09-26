# Question:
# Shape hierarchy: Shape -> Polygon -> Triangle, Rectangle
# Each class adds specific area() computation.

import math

class Shape:
    def area(self):
        return 0
    def name(self):
        return "Shape"

class Polygon(Shape):
    def __init__(self, sides):
        self.sides = sides
    def name(self):
        return f"Polygon({self.sides} sides)"

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def name(self):
        return f"Triangle(base={self.base}, height={self.height})"

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def name(self):
        return f"Rectangle(width={self.width}, height={self.height})"

shapes = [Triangle(6, 4), Rectangle(5, 3)]
for s in shapes:
    print(f"{s.name()} -> Area = {s.area():.2f}")
