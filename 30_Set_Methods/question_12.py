# Question:
# Use difference_update() to remove from set A all elements that are in B.
# This modifies A in place.

A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8}

print(f"Before: A = {A}")
print(f"        B = {B}")

A.difference_update(B)
print(f"After A.difference_update(B): A = {A}")
print("Elements present in B were removed from A.")
