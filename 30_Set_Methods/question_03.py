# Question:
# Create a set of 5 animals.
# Use remove() to remove an existing element.
# Then try to remove a non-existent element (shows KeyError).
# Use discard() to safely remove without error.

animals = {"cat", "dog", "fish", "bird", "rabbit"}
print(f"Original: {animals}")

# remove() - raises KeyError if element not found
animals.remove("fish")
print(f"After remove('fish'): {animals}")

try:
    animals.remove("lion")  # Not in set
except KeyError as e:
    print(f"KeyError from remove('lion'): {e}")

# discard() - safe, no error if not found
animals.discard("lion")
print(f"After discard('lion') - no error: {animals}")

animals.discard("cat")
print(f"After discard('cat'): {animals}")
