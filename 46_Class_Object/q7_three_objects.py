# Question: Create 3 objects of the same class, each with different data.
# Show that all three are independent instances of the same class.

# Example output:
# Student 1: Alice  - GPA: 3.8
# Student 2: Bob    - GPA: 3.2
# Student 3: Carol  - GPA: 3.9
# 
# All are Student objects: True
# Best student: Carol (GPA: 3.9)

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def info(self):
        return f"{self.name:<8} - GPA: {self.gpa}"

# Create 3 different objects from the same class
s1 = Student("Alice", 3.8)
s2 = Student("Bob", 3.2)
s3 = Student("Carol", 3.9)

print(f"Student 1: {s1.info()}")
print(f"Student 2: {s2.info()}")
print(f"Student 3: {s3.info()}")

# All are instances of Student
print(f"\nAll are Student objects: {isinstance(s1, Student) and isinstance(s2, Student) and isinstance(s3, Student)}")

# Find best student
students = [s1, s2, s3]
best = max(students, key=lambda s: s.gpa)
print(f"Best student: {best.name} (GPA: {best.gpa})")
