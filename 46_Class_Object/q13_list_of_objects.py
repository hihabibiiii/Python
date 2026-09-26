# Question: Create a list of objects and iterate over them.
# Create multiple Student objects, store in a list, and iterate to print info.

# Example output:
# All students:
# 1. Alice    | GPA: 3.8 | Major: Computer Science
# 2. Bob      | GPA: 3.2 | Major: Mathematics
# 3. Carol    | GPA: 3.9 | Major: Physics
# 4. David    | GPA: 3.5 | Major: Engineering
# 
# Students with GPA >= 3.5:
# - Alice (3.8)
# - Carol (3.9)
# - David (3.5)

class Student:
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major

    def info(self):
        return f"{self.name:<8} | GPA: {self.gpa} | Major: {self.major}"

# Create a list of Student objects
students = [
    Student("Alice", 3.8, "Computer Science"),
    Student("Bob", 3.2, "Mathematics"),
    Student("Carol", 3.9, "Physics"),
    Student("David", 3.5, "Engineering"),
    Student("Eve", 2.9, "Biology"),
]

# Iterate over the list of objects
print("All students:")
for i, student in enumerate(students, 1):
    print(f"  {i}. {student.info()}")

# Filter: students with GPA >= 3.5
print("\nStudents with GPA >= 3.5:")
for student in students:
    if student.gpa >= 3.5:
        print(f"  - {student.name} ({student.gpa})")

# Find best student using list iteration
best = students[0]
for s in students:
    if s.gpa > best.gpa:
        best = s
print(f"\nBest student: {best.name} ({best.gpa})")
