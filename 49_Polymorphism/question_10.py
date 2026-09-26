# Question:
# Override __lt__ for comparison and use sorted() on a list of custom objects.

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __lt__(self, other):
        return self.gpa < other.gpa  # Compare by GPA

    def __str__(self):
        return f"{self.name} (GPA: {self.gpa})"

students = [
    Student("Alice", 3.5),
    Student("Bob", 3.8),
    Student("Charlie", 3.2),
    Student("Diana", 3.9),
    Student("Eve", 3.6),
]

print("Unsorted:")
for s in students:
    print(f"  {s}")

students_sorted = sorted(students)  # Uses __lt__
print("\nSorted by GPA (ascending):")
for s in students_sorted:
    print(f"  {s}")
