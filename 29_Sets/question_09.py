# Question:
# Create two sets A and B.
# Check if A is a subset of B and if B is a superset of A.

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(f"A = {A}")
print(f"B = {B}")

print(f"A is subset of B: {A.issubset(B)}")
print(f"B is superset of A: {B.issuperset(A)}")
print(f"B is subset of A: {B.issubset(A)}")
print(f"A is superset of B: {A.issuperset(B)}")
