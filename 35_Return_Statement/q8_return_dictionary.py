# Question 8 (Medium):
# Define a function called get_student_info that takes name, age, and grade
# and returns a DICTIONARY containing all that information.

# Solution:
def get_student_info(name, age, grade):
    return {
        "name": name,
        "age": age,
        "grade": grade
    }

# Test with examples
student1 = get_student_info("Alice", 20, "A")
student2 = get_student_info("Bob", 22, "B+")

print("Student 1:", student1)
print("Student 2:", student2)

# Get info from user
print("\nEnter student information:")
name = input("Name: ").strip()
age = int(input("Age: "))
grade = input("Grade: ").strip()

info = get_student_info(name, age, grade)
print("\nStudent record:")
for key, value in info.items():
    print(f"  {key}: {value}")

# Example Output:
# Student 1: {'name': 'Alice', 'age': 20, 'grade': 'A'}
