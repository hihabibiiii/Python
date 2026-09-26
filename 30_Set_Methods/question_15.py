# Question:
# Perform a chain of set operations:
# Start with set A.
# Union with B -> then Intersect with C -> then Remove elements of D.
# Print the set after each step.

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {1, 3, 5, 6, 7, 9}
D = {5, 6}

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"D = {D}")
print()

step1 = A.union(B)
print(f"Step 1 (A union B):         {step1}")

step2 = step1.intersection(C)
print(f"Step 2 (intersect with C):  {step2}")

step3 = step2.difference(D)
print(f"Step 3 (remove elements D): {step3}")

print(f"\nFinal result: {step3}")
