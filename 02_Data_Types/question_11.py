# Question 11 (Hard):
# Create a nested data structure: a dictionary where each key is a
# student name and each value is a list of their marks.
# Print each student's name and their individual marks.
# Also print the first student's second mark.

# Solution:
students = {
    "Alice": [85, 90, 78],
    "Bob": [72, 65, 80],
    "Charlie": [95, 88, 92]
}

for student, marks in students.items():
    print(f"{student}: {marks}")

print("\nFirst student's second mark:", students["Alice"][1])

# Output:
# Alice: [85, 90, 78]
# Bob: [72, 65, 80]
# Charlie: [95, 88, 92]
#
# First student's second mark: 90
