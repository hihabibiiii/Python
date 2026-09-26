# Question: Create a class Circle with attribute radius and method area().
# Compute the area using pi * r^2.

# Example output:
# Circle with radius 5
# Area: 78.54 sq units
# Circumference: 31.42 units

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def display(self):
        print(f"Circle with radius {self.radius}")
        print(f"Area:          {self.area():.2f} sq units")
        print(f"Circumference: {self.circumference():.2f} units")

# Create a circle
r = float(input("Enter radius: "))
c = Circle(r)
c.display()
