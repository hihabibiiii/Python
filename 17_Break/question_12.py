# Question:
# Search for a value in a 3x3 matrix (list of lists).
# Use nested loops with break to stop when the value is found.
# Print the row and column of the found value.

# Example:
# Searching for: 7
# Found 7 at row 1, column 0.

matrix = [
    [1, 2, 3],
    [7, 5, 6],
    [4, 8, 9]
]

target = int(input("Enter value to search: "))
found = False

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == target:
            print(f"Found {target} at row {r}, column {c}.")
            found = True
            break
    if found:
        break

if not found:
    print(f"{target} not found in the matrix.")
