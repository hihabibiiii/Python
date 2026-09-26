# Question:
# Create a base class Shape with a method describe().
# Create a child class Circle that overrides the describe() method.

class Shape:
    def describe(self):
        return "I am a generic shape."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def describe(self):
        # Override parent method
        return f"I am a Circle with radius {self.radius}."

s = Shape()
c = Circle(5)

print(s.describe())
print(c.describe())
