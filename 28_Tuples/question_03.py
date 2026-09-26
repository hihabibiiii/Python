# Question:
# Create a tuple of 3 elements.
# Try to modify one of its elements.
# Show that it raises a TypeError (tuples are immutable).

# Example Output:
# Original tuple: (1, 2, 3)
# Trying to change element...
# Error: 'tuple' object does not support item assignment

my_tuple = (1, 2, 3)
print(f"Original tuple: {my_tuple}")
print("Trying to change element at index 0...")

try:
    my_tuple[0] = 99
except TypeError as e:
    print(f"Error: {e}")

print("Tuples are immutable - their elements cannot be changed.")
