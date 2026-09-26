# Question:
# Use the intersection() method to find common elements between two sets.
# Also compare with intersection_update() which modifies in place.

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

print(f"A = {A}")
print(f"B = {B}")

# intersection() - returns new set
common = A.intersection(B)
print(f"A.intersection(B) = {common}")
print(f"A unchanged: {A}")
