# Question:
# Create a set and use copy() to make a copy of it.
# Modify the original set and show the copy is unaffected.

original = {10, 20, 30, 40}
print(f"Original: {original}")

copy_set = original.copy()
print(f"Copy:     {copy_set}")

# Modify original
original.add(50)
original.remove(10)

print(f"\nAfter modifying original:")
print(f"Original: {original}")
print(f"Copy:     {copy_set}  <- unchanged!")
