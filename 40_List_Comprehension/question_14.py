# Question:
# Transpose a matrix (list of lists) using nested list comprehension.
# Transposing swaps rows and columns.
# [[1,2,3],[4,5,6]] -> [[1,4],[2,5],[3,6]]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(" ", row)

transposed = [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]

print("\nTransposed matrix:")
for row in transposed:
    print(" ", row)
