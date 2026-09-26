# Question:
# Read-only property: define getter but NO setter.
# Attempting to set raises AttributeError.

class ImmutablePoint:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def distance_from_origin(self):
        return (self.__x**2 + self.__y**2) ** 0.5

    def __str__(self):
        return f"Point({self.__x}, {self.__y})"

p = ImmutablePoint(3, 4)
print(p)
print(f"x = {p.x}")
print(f"y = {p.y}")
print(f"Distance from origin = {p.distance_from_origin:.4f}")

# Try to set - should raise AttributeError
try:
    p.x = 10
except AttributeError as e:
    print(f"\nError: {e}")
    print("This is a read-only property!")
