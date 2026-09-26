# Question:
# Create a set of 3 numbers.
# Use update() to add multiple new elements at once.
# Print before and after.

# update() accepts any iterable.

numbers = {1, 2, 3}
print(f"Before update: {numbers}")

numbers.update([4, 5, 6])
print(f"After update([4,5,6]): {numbers}")

numbers.update({7, 8}, (9, 10))
print(f"After update with set and tuple: {numbers}")
