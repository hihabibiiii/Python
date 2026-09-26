# Question 13 (Hard):
# Create a nested dictionary representing a student record.
# The student should have: name, age, and a nested dictionary called 'subjects'
# with at least 3 subjects and their marks.
# Print the student's name and all subject marks.

# Solution:
student = {
    "name": "Henry",
    "age": 19,
    "subjects": {
        "Mathematics": 88,
        "Physics": 75,
        "Chemistry": 92,
        "English": 81
    }
}

print(f"Student Name: {student['name']}")
print(f"Age: {student['age']}")
print("\nSubject Marks:")
print("-" * 25)
for subject, marks in student["subjects"].items():
    print(f"  {subject:<15}: {marks}")

# Calculate average
avg = sum(student["subjects"].values()) / len(student["subjects"])
print(f"\nAverage Marks: {avg:.2f}")

# Example Output:
# Student Name: Henry
# Age: 19
#
# Subject Marks:
# -------------------------
#   Mathematics    : 88
#   Physics        : 75
#   Chemistry      : 92
#   English        : 81
#
# Average Marks: 84.00
