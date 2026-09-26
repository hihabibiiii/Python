# Question:
# Use the union() method to combine two sets.
# union() returns a NEW set without modifying the originals.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A = {A}")
print(f"B = {B}")

result = A.union(B)
print(f"A.union(B) = {result}")
print(f"A unchanged: {A}")
print(f"B unchanged: {B}")
