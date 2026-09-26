# Question:
# Create a tuple of tuples representing a 3x3 matrix.
# Iterate over all values and print them.

# Example Output:
# 1 2 3
# 4 5 6
# 7 8 9

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Matrix:")
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
