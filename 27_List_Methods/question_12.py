# Question:
# Use sort() with the key parameter to sort a list of strings by their length.

# Example:
# Original: ["banana", "kiwi", "apple", "fig", "elderberry"]
# Sorted by length: ["fig", "kiwi", "apple", "banana", "elderberry"]

fruits = ["banana", "kiwi", "apple", "fig", "elderberry"]
print(f"Original: {fruits}")

fruits.sort(key=len)
print(f"Sorted by length: {fruits}")
