# Question:
# Override __mul__ for a Vector class to support scalar multiplication.
# v * 3 should multiply each component by 3.

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

v = Vector(1, 2, 3)
print(f"v = {v}")
print(f"|v| = {v.magnitude():.4f}")

v2 = v * 3
print(f"v * 3 = {v2}")
print(f"|v*3| = {v2.magnitude():.4f}")

v3 = 2 * v
print(f"2 * v = {v3}")
