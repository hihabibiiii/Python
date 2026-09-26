# Question: Create a list of tuples [(name, score)] for 5 students.
#           Print the names of students scoring above 70.
# Example:
#   students = [("Alice", 85), ("Bob", 60), ("Carol", 92), ("Dave", 70), ("Eve", 78)]
#   Output: Students scoring above 70: Alice, Carol, Eve

students = [
    ("Alice", 85),
    ("Bob", 60),
    ("Carol", 92),
    ("Dave", 70),
    ("Eve", 78)
]

print("All students:", students)
print("\nStudents scoring above 70:")
for name, score in students:
    if score > 70:
        print(f"  {name} - Score: {score}")
