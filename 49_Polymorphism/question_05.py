# Question:
# Create Shape, Circle, and Rectangle classes.
# Each has an area() method.
# Call area() polymorphically using a loop.

import math

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

shapes = [Shape(), Circle(7), Rectangle(4, 5), Square(6)]

print("Polymorphic area computation:")
for shape in shapes:
    print(f"  {type(shape).__name__:<12}: area = {shape.area():.4f}")
