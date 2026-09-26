# Question:
# Create sets A, B, and C.
# Use issubset() and issuperset() to check relationships.

A = {1, 2}
B = {1, 2, 3, 4}
C = {1, 2, 3, 4, 5}

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")

print(f"A.issubset(B)    : {A.issubset(B)}")   # True
print(f"B.issubset(C)    : {B.issubset(C)}")   # True
print(f"C.issuperset(B)  : {C.issuperset(B)}") # True
print(f"B.issuperset(A)  : {B.issuperset(A)}") # True
print(f"A.issubset(C)    : {A.issubset(C)}")   # True
print(f"C.issubset(A)    : {C.issubset(A)}")   # False
