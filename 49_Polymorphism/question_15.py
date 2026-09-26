# Question:
# Create a full shape hierarchy where area(), perimeter(), and __str__
# are all overridden. Print a formatted shape report.

import math

class Shape:
    def area(self):
        return 0
    def perimeter(self):
        return 0
    def __str__(self):
        return f"{type(self).__name__:<12} | Area: {self.area():>10.4f} | Perimeter: {self.perimeter():>10.4f}"

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r**2
    def perimeter(self):
        return 2 * math.pi * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))
    def perimeter(self):
        return self.a + self.b + self.c

shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5),
    Circle(10),
    Rectangle(7, 2),
]

print("Shape Report")
print("=" * 55)
print(f"{'Shape':<12} | {'Area':>14} | {'Perimeter':>14}")
print("-" * 55)
for shape in shapes:
    print(shape)
print("=" * 55)
