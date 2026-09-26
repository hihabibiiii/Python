# Question:
# Use @property decorator to create a getter.
# Access private attribute as if it were a public attribute.

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        """Getter for radius."""
        return self.__radius

    @property
    def area(self):
        """Computed property for area."""
        import math
        return math.pi * self.__radius ** 2

c = Circle(5)

# Access like an attribute (no parentheses needed)
print(f"Radius: {c.radius}")
print(f"Area:   {c.area:.4f}")

# Try to set directly (will fail - no setter defined)
try:
    c.radius = 10
except AttributeError as e:
    print(f"Error setting radius: {e}")
