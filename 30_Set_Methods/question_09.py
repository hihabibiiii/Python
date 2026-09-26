# Question:
# Use symmetric_difference() to find elements in A or B but NOT both.
# Returns a new set.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A = {A}")
print(f"B = {B}")

sym = A.symmetric_difference(B)
print(f"A.symmetric_difference(B) = {sym}")
print("These are in one set but not the other.")
