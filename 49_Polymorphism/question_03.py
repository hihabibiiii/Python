# Question:
# Create a list of different objects.
# Call the same method on each (polymorphic behavior).

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        import math
        return math.pi * self.r**2

class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

class Triangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return 0.5 * self.b * self.h

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

print("Polymorphic area() calls:")
for shape in shapes:
    print(f"  {type(shape).__name__:<12} area = {shape.area():.2f}")
