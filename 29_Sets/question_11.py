# Question:
# Ask the user to enter two comma-separated lists of numbers.
# Convert each to a set and find the common elements (intersection).
# Print the common elements.

# Example:
# Enter first list: 1,2,3,4,5
# Enter second list: 3,4,5,6,7
# Common elements: {3, 4, 5}

raw1 = input("Enter first list (comma-separated): ")
raw2 = input("Enter second list (comma-separated): ")

set1 = set(int(x.strip()) for x in raw1.split(","))
set2 = set(int(x.strip()) for x in raw2.split(","))

common = set1 & set2
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Common elements: {common}")
