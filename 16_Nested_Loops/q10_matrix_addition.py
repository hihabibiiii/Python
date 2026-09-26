# Question:
# Add two 3x3 matrices hardcoded as lists and print the result using nested loops.
#
# Matrix A:        Matrix B:
#  1  2  3          9  8  7
#  4  5  6          6  5  4
#  7  8  9          3  2  1
#
# Expected Result:
#  10 10 10
#  10 10 10
#  10 10 10

matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Create result matrix (3x3 of zeros)
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Add matrices using nested loops
for i in range(3):
    for j in range(3):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]

print("Matrix A:")
for row in matrix_a:
    print(row)

print("\nMatrix B:")
for row in matrix_b:
    print(row)

print("\nResult (A + B):")
for row in result:
    print(row)
