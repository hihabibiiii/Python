# Question:
# Create two sets A and B.
# Find their union using | operator and union() method.
# Print both results.

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"A = {A}")
print(f"B = {B}")

# Using | operator
union_op = A | B
print(f"A | B = {union_op}")

# Using union() method
union_method = A.union(B)
print(f"A.union(B) = {union_method}")
