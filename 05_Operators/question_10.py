# Question 10 (Medium):
# Create two sets and use set operators:
#   & (intersection), | (union), - (difference)
# Print results.

# Solution:
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)
print()
print("A & B (Intersection):", set_a & set_b)
print("A | B (Union)       :", set_a | set_b)
print("A - B (Difference)  :", set_a - set_b)
print("B - A (Difference)  :", set_b - set_a)

# Output:
# Set A: {1, 2, 3, 4, 5}
# Set B: {4, 5, 6, 7, 8}
#
# A & B (Intersection): {4, 5}
# A | B (Union)       : {1, 2, 3, 4, 5, 6, 7, 8}
# A - B (Difference)  : {1, 2, 3}
# B - A (Difference)  : {8, 6, 7}
