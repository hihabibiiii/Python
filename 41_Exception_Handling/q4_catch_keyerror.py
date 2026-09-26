# Question: Create a dictionary of student grades. Ask the user to enter a student name.
# Use try/except to catch KeyError if the name is not found in the dictionary,
# and print a helpful message.

# Example:
# Students: {'Alice': 90, 'Bob': 85, 'Charlie': 92}
# Enter a student name: Dave
# Error: 'Dave' not found in the grade book!

# Enter a student name: Alice
# Alice's grade: 90

students = {'Alice': 90, 'Bob': 85, 'Charlie': 92}
print(f"Students: {students}")

try:
    name = input("Enter a student name: ")
    grade = students[name]
    print(f"{name}'s grade: {grade}")
except KeyError:
    print(f"Error: '{name}' not found in the grade book!")
