# Question: Update a specific cell in a 2D list using row and column indices from the user.
# Example:
#   grid[1][2] = 99 -> changes second row, third column to 99

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original grid:")
for row in grid:
    print(row)

row = int(input("\nEnter the row index (0-2): "))
col = int(input("Enter the column index (0-2): "))
new_value = int(input("Enter the new value: "))

grid[row][col] = new_value

print(f"\nUpdated grid[{row}][{col}] = {new_value}:")
for r in grid:
    print(r)
