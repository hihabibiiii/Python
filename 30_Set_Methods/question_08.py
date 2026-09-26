# Question:
# Use the difference() method to find elements in A but NOT in B.
# difference() returns a new set.

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

print(f"A = {A}")
print(f"B = {B}")

diff = A.difference(B)
print(f"A.difference(B) = {diff}  (in A but not B)")

diff2 = B.difference(A)
print(f"B.difference(A) = {diff2}  (in B but not A)")
