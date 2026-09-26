# Question: Student Grade Book — take 5 student names and marks via input(),
# write the data to a file, then read the file and print a formatted grade report.

# Example output:
# === Student Grade Book ===
# Enter details for 5 students:
# Student 1 name: Alice
# Alice's marks: 88
# ...
# 
# Data saved to 'gradebook.txt'
# 
# === GRADE REPORT ===
# -----------------------------------------------
# Name            Marks  Grade   Status
# -----------------------------------------------
# Alice           88     B       Pass
# ...
# -----------------------------------------------
# Class Average: 82.4

def get_grade(marks):
    """Return letter grade based on marks."""
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

print("=" * 35)
print("      Student Grade Book")
print("=" * 35)
print("Enter details for 5 students:\n")

# Collect student data
students = []
for i in range(1, 6):
    name = input(f"Student {i} name: ").strip()
    while True:
        try:
            marks = int(input(f"{name}'s marks (0-100): "))
            if 0 <= marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid integer.")
    students.append((name, marks))

# Write to file
with open('gradebook.txt', 'w') as f:
    f.write("Name,Marks\n")
    for name, marks in students:
        f.write(f"{name},{marks}\n")

print("\nData saved to 'gradebook.txt'")

# Read and display formatted report
print("\n" + "=" * 47)
print("              GRADE REPORT")
print("=" * 47)
print(f"{'Name':<15} {'Marks':<7} {'Grade':<8} {'Status'}")
print("-" * 47)

total_marks = 0
with open('gradebook.txt', 'r') as f:
    next(f)  # Skip header
    for line in f:
        name, marks = line.strip().split(',')
        marks = int(marks)
        grade = get_grade(marks)
        status = "Pass" if marks >= 50 else "Fail"
        total_marks += marks
        print(f"{name:<15} {marks:<7} {grade:<8} {status}")

print("-" * 47)
avg = total_marks / len(students)
print(f"Class Average: {avg:.1f}")
