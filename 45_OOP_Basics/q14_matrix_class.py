# Question: Create a class Matrix2x2 representing a 2x2 matrix.
# Add methods add() and multiply() with another Matrix2x2.

# A 2x2 matrix: [[a, b], [c, d]]
# Addition: add element by element
# Multiplication: standard matrix multiplication

class Matrix2x2:
    def __init__(self, a, b, c, d):
        # [[a, b], [c, d]]
        self.matrix = [[a, b], [c, d]]

    def display(self):
        for row in self.matrix:
            print(f"  | {row[0]:5} {row[1]:5} |")

    def add(self, other):
        """Add two 2x2 matrices element by element."""
        a = self.matrix[0][0] + other.matrix[0][0]
        b = self.matrix[0][1] + other.matrix[0][1]
        c = self.matrix[1][0] + other.matrix[1][0]
        d = self.matrix[1][1] + other.matrix[1][1]
        return Matrix2x2(a, b, c, d)

    def multiply(self, other):
        """Multiply two 2x2 matrices (standard matrix multiplication)."""
        a = self.matrix[0][0] * other.matrix[0][0] + self.matrix[0][1] * other.matrix[1][0]
        b = self.matrix[0][0] * other.matrix[0][1] + self.matrix[0][1] * other.matrix[1][1]
        c = self.matrix[1][0] * other.matrix[0][0] + self.matrix[1][1] * other.matrix[1][0]
        d = self.matrix[1][0] * other.matrix[0][1] + self.matrix[1][1] * other.matrix[1][1]
        return Matrix2x2(a, b, c, d)

# Create two matrices
m1 = Matrix2x2(1, 2, 3, 4)
m2 = Matrix2x2(5, 6, 7, 8)

print("Matrix 1:")
m1.display()

print("\nMatrix 2:")
m2.display()

print("\nM1 + M2 (Addition):")
result_add = m1.add(m2)
result_add.display()

print("\nM1 × M2 (Multiplication):")
result_mul = m1.multiply(m2)
result_mul.display()
