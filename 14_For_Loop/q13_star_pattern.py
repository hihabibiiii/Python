# Question:
# Print a right-aligned triangle pattern of stars with 5 rows using a for loop.
# Each row should be right-aligned so stars line up on the right.
#
# Expected Output:
#     *
#    **
#   ***
#  ****
# *****

rows = 5
print("Right-aligned triangle of stars:")
for i in range(1, rows + 1):
    # Print spaces first, then stars
    spaces = rows - i
    stars = i
    print(" " * spaces + "*" * stars)
