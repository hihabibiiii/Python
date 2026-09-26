# Question: Use copy() to make a shallow copy of a list.
# Modify the original list and show that the copy is unaffected.
# Example:
#   original = [1, 2, 3]
#   copy_ = original.copy()
#   original.append(99)
#   original -> [1, 2, 3, 99]  (modified)
#   copy_    -> [1, 2, 3]      (unchanged)

original = [1, 2, 3, 4, 5]
copy_ = original.copy()

print("Original:", original)
print("Copy:    ", copy_)

# Modify the original
original.append(99)
original[0] = 100

print("\nAfter modifying original:")
print("Original:", original)
print("Copy (unaffected):", copy_)
