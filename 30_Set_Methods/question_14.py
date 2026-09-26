# Question:
# Create a frozenset (immutable set).
# Show that it supports set operations (union, intersection, etc.)
# but does NOT support add(), remove(), etc.

fs = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {fs}")
print(f"Type: {type(fs)}")

# Set operations work on frozenset
other = frozenset([4, 5, 6, 7])
print(f"Union: {fs | other}")
print(f"Intersection: {fs & other}")

# Trying to add raises AttributeError
try:
    fs.add(6)
except AttributeError as e:
    print(f"\nError when using add(): {e}")
    print("Frozensets are immutable - cannot be modified!")
