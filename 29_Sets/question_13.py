# Question:
# Create two sets and check if they are disjoint.
# Disjoint = they have NO common elements.
# Use isdisjoint() method.

A = {1, 2, 3}
B = {4, 5, 6}
C = {3, 4, 5}

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")

print(f"A and B are disjoint: {A.isdisjoint(B)}")  # True
print(f"A and C are disjoint: {A.isdisjoint(C)}")  # False (both have 3)
