# Question:
# Create two sets A and B.
# Find their intersection using & and intersection().
# Intersection = elements present in BOTH sets.

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

print(f"A = {A}")
print(f"B = {B}")

# Using & operator
intersect_op = A & B
print(f"A & B = {intersect_op}")

# Using intersection() method
intersect_method = A.intersection(B)
print(f"A.intersection(B) = {intersect_method}")
