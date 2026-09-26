# Question:
# Override __eq__ to compare two custom objects for equality.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 2)

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p3 = {p3}")
print(f"p1 == p2: {p1 == p2}")  # True (same coordinates)
print(f"p1 == p3: {p1 == p3}")  # False
print(f"p1 is p2: {p1 is p2}")  # False (different objects)
