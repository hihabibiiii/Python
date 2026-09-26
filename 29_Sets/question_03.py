# Question:
# Create a set of 5 numbers.
# Remove an element using remove().
# Demonstrate that removing a non-existent element raises KeyError.
# Use discard() as a safer alternative.

numbers = {10, 20, 30, 40, 50}
print(f"Original: {numbers}")

numbers.remove(30)
print(f"After remove(30): {numbers}")

# remove() raises KeyError for non-existent element
try:
    numbers.remove(99)
except KeyError as e:
    print(f"remove(99) raised KeyError: {e}")

# discard() does NOT raise an error
numbers.discard(99)
print(f"After discard(99) - no error: {numbers}")
