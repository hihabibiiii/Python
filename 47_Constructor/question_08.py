# Question:
# Create classes Point and Circle.
# Circle's __init__ takes a Point object (center) and a radius.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Circle:
    def __init__(self, center, radius):
        self.center = center  # Takes another object as parameter
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(center={self.center}, radius={self.radius})"

center = Point(3, 4)
c = Circle(center, 5)
print(c)
print(f"Area: {c.area():.4f}")
print(f"Center coordinates: x={c.center.x}, y={c.center.y}")
