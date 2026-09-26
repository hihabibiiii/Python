# Question:
# Create an empty set and use add() to add 5 elements one by one.
# Print the set after each addition.

# Note: {} creates a dict, not a set. Use set() for an empty set.

my_set = set()

my_set.add(10)
print(f"After add(10): {my_set}")

my_set.add(20)
print(f"After add(20): {my_set}")

my_set.add(30)
print(f"After add(30): {my_set}")

my_set.add(10)  # Duplicate - no change
print(f"After add(10) again: {my_set}")

my_set.add(40)
print(f"After add(40): {my_set}")
