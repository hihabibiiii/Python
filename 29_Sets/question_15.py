# Question:
# A list of student names is given (with duplicates from multiple submissions).
# Use a set to find the unique student names.
# Print the unique names and the total count.

# Example Output:
# Unique students: 4

submissions = [
    "Alice", "Bob", "Charlie", "Alice",
    "Diana", "Bob", "Alice", "Charlie"
]

print(f"Total submissions: {len(submissions)}")

unique_students = set(submissions)
print(f"Unique students ({len(unique_students)}):")
for name in sorted(unique_students):
    print(f"  {name}")
