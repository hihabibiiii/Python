# Question:
# Create two sets A and B.
# Find the difference A - B (elements in A but NOT in B).
# Also find B - A.

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

print(f"A = {A}")
print(f"B = {B}")

diff_AB = A - B
print(f"A - B = {diff_AB}  (in A but not B)")

diff_BA = B - A
print(f"B - A = {diff_BA}  (in B but not A)")
