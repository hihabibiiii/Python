# Question: Store objects in a dictionary mapping name → object.
# Create Student objects and look them up by name.

# Example output:
# Students in database:
# Alice   → GPA: 3.8, Major: CS
# Bob     → GPA: 3.2, Major: Math
# Carol   → GPA: 3.9, Major: Physics
# 
# Looking up 'Alice': GPA 3.8 in CS
# Looking up 'Dave': Not found!

class Student:
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major

    def info(self):
        return f"GPA: {self.gpa}, Major: {self.major}"

# Store objects in a dictionary: name → object
student_db = {
    "Alice": Student("Alice", 3.8, "CS"),
    "Bob":   Student("Bob", 3.2, "Math"),
    "Carol": Student("Carol", 3.9, "Physics"),
    "David": Student("David", 3.5, "Engineering"),
}

# Iterate over dictionary of objects
print("Students in database:")
for name, student in student_db.items():
    print(f"  {name:<8} → {student.info()}")

# Look up by name
print()
for query in ["Alice", "Carol", "Dave"]:
    if query in student_db:
        s = student_db[query]
        print(f"Looking up '{query}': GPA {s.gpa} in {s.major}")
    else:
        print(f"Looking up '{query}': Not found!")
