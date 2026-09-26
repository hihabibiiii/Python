# Question:
# Print an inverted right triangle pattern of stars using nested loops.
# Start with 5 stars and decrease by one each row.
#
# Expected Output:
#   *****
#   ****
#   ***
#   **
#   *

rows = 5
print("Inverted right triangle of stars:")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
