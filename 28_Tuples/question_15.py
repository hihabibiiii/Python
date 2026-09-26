# Question:
# Create student records using plain tuples: (name, age, grade).
# Store 3 students and print a formatted report.

# Example Output:
# Student Report
# ===============
# Name: Alice  | Age: 20 | Grade: A
# Name: Bob    | Age: 22 | Grade: B
# Name: Charlie| Age: 21 | Grade: A+

students = [
    ("Alice", 20, "A"),
    ("Bob", 22, "B"),
    ("Charlie", 21, "A+")
]

print("Student Report")
print("=" * 40)
for student in students:
    name, age, grade = student
    print(f"Name: {name:<10} | Age: {age} | Grade: {grade}")
