# Question 8 (Medium):
# Demonstrate the copy() method to make a shallow copy of a dictionary.
# Show that modifying the copy does NOT affect the original.

# Solution:
original = {
    "name": "Diana",
    "scores": [85, 90, 78],
    "grade": "B+"
}

# Make a shallow copy
copy_dict = original.copy()

print("Original:", original)
print("Copy:    ", copy_dict)

# Modify a simple value in copy — original is NOT affected
copy_dict["grade"] = "A"
print("\nAfter changing 'grade' in copy:")
print("Original grade:", original["grade"])
print("Copy grade:    ", copy_dict["grade"])

# CAUTION: Shallow copy — nested objects are still shared
copy_dict["scores"].append(95)
print("\nAfter appending to 'scores' list in copy:")
print("Original scores:", original["scores"])  # Also changed!
print("Copy scores:    ", copy_dict["scores"])

print("\nNote: For deep copy of nested objects, use copy.deepcopy()")

# Example Output:
# Original grade: B+
# Copy grade:     A
# Original scores: [85, 90, 78, 95]  <-- also changed!
# Copy scores:     [85, 90, 78, 95]
