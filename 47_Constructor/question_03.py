# Question:
# Create a class Rectangle with __init__ that has default parameter values.
# width defaults to 1, height defaults to 1.

class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r1 = Rectangle()         # default
r2 = Rectangle(5, 3)    # custom
r3 = Rectangle(width=4) # partial

print(f"r1: width={r1.width}, height={r1.height}, area={r1.area()}")
print(f"r2: width={r2.width}, height={r2.height}, area={r2.area()}")
print(f"r3: width={r3.width}, height={r3.height}, area={r3.area()}")
