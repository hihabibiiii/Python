# Question:
# Print a diamond pattern of stars using nested loops.
# The diamond should have 5 rows going up and 4 rows going down.
#
# Expected Output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

rows = 5
print("Diamond pattern of stars:")

# Upper half (including middle)
for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# Lower half
for i in range(rows - 1, 0, -1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
