# Question:
# Create two sets A and B.
# Find elements that are in A or B but NOT in both (symmetric difference).
# Use the ^ operator.

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print(f"A = {A}")
print(f"B = {B}")

sym_diff = A ^ B
print(f"Symmetric difference (A ^ B): {sym_diff}")
print("These elements are in one set but not both.")
