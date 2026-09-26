# Question:
# Create a set of 3 fruits.
# Add a new fruit using add().
# Print the set before and after adding.

fruits = {"apple", "banana", "cherry"}
print(f"Before: {fruits}")

fruits.add("mango")
print(f"After adding 'mango': {fruits}")

# Adding a duplicate - no change
fruits.add("apple")
print(f"After adding duplicate 'apple': {fruits}")
