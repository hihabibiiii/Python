# Question: Given a 3x3 matrix as a list of lists, print the diagonal elements.
# Diagonal elements are where row index == column index: [0][0], [1][1], [2][2].
# Example:
#   Matrix:
#     1  2  3
#     4  5  6
#     7  8  9
#   Diagonal: 1, 5, 9

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print("\nDiagonal elements (top-left to bottom-right):")
for i in range(3):
    print(f"  matrix[{i}][{i}] = {matrix[i][i]}")
