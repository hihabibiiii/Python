# Question:
# Create two sets A and B.
# Find their symmetric difference (elements in A or B but NOT in both).
# Use ^ operator and symmetric_difference() method.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A = {A}")
print(f"B = {B}")

sym_diff = A ^ B
print(f"A ^ B = {sym_diff}")

sym_diff2 = A.symmetric_difference(B)
print(f"A.symmetric_difference(B) = {sym_diff2}")
