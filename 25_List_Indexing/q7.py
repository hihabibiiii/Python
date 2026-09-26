# Question: Access elements of a nested list (2D list) using indexing.
# Use two indices: [row][column] to access elements.
# Example:
#   matrix[1][2] -> second row, third column

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("2D List (Matrix):")
for row in matrix:
    print(row)

print("\nAccessing individual elements:")
print("matrix[0][0]:", matrix[0][0])   # top-left
print("matrix[1][2]:", matrix[1][2])   # second row, third column
print("matrix[2][1]:", matrix[2][1])   # bottom middle
