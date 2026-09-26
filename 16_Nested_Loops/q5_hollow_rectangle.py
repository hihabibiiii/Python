# Question:
# Print a hollow rectangle of stars (border only) using nested loops.
# The rectangle should be 5 rows tall and 8 columns wide.
# Only print stars on the border; the inside should be spaces.
#
# Expected Output:
#   ********
#   *      *
#   *      *
#   *      *
#   ********

rows = 5
cols = 8

print("Hollow rectangle of stars:")
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
