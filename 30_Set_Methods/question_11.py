# Question:
# Use intersection_update() to update set A in place.
# A keeps only elements that are also in B.

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

print(f"Before: A = {A}")
print(f"        B = {B}")

A.intersection_update(B)
print(f"After A.intersection_update(B): A = {A}")
print("A now contains only elements that were in both A and B.")
