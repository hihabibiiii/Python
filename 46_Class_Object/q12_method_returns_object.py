# Question: Create a class with a method that creates and returns another object of the same class.
# This is the "factory method" pattern: an object creates another object of its own type.

# Example output:
# Original: Point(3, 4)
# Reflected across X-axis: Point(3, -4)
# Reflected across Y-axis: Point(-3, 4)
# Origin: Point(0, 0)

class Point:
    """Represents a 2D point."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def reflect_x(self):
        """Returns a NEW Point reflected across the X-axis (y flips sign)."""
        return Point(self.x, -self.y)   # Creates and returns a new Point object

    def reflect_y(self):
        """Returns a NEW Point reflected across the Y-axis (x flips sign)."""
        return Point(-self.x, self.y)

    def midpoint(self, other):
        """Returns the midpoint between this Point and another Point."""
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point(mx, my)  # Returns a new Point object

    @classmethod
    def origin(cls):
        """Class method: creates a Point at (0, 0)."""
        return cls(0, 0)

# Test
p1 = Point(3, 4)
print(f"Original:                  {p1}")
print(f"Reflected across X-axis:   {p1.reflect_x()}")
print(f"Reflected across Y-axis:   {p1.reflect_y()}")

p2 = Point(7, 2)
mid = p1.midpoint(p2)
print(f"\nMidpoint of {p1} and {p2}: {mid}")

origin = Point.origin()
print(f"Origin point: {origin}")
