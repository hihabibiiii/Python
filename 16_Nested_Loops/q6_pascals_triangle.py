# Question:
# Print Pascal's Triangle for 5 rows using nested loops.
# Each number is the sum of the two numbers directly above it.
# Row 0:    1
# Row 1:   1 1
# Row 2:  1 2 1
# Row 3: 1 3 3 1
# Row 4:1 4 6 4 1

print("Pascal's Triangle (5 rows):")

rows = 5
# Build Pascal's triangle row by row
triangle = []
for i in range(rows):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    triangle.append(row)

# Print the triangle
for i in range(rows):
    # Add leading spaces for alignment
    print(" " * (rows - i - 1), end="")
    for num in triangle[i]:
        print(f"{num} ", end="")
    print()
