# Question 13 (Hard):
# Take total marks and number of subjects from the user.
# Compute the percentage: (total_marks / (subjects * 100)) * 100
# Print percentage and grade: A (>=90), B (>=80), C (>=70), D (>=60), F (<60).

# Solution:
total_marks = float(input("Enter total marks obtained: "))
subjects = int(input("Enter number of subjects : "))

max_marks = subjects * 100
percentage = (total_marks / max_marks) * 100

print(f"\nTotal Marks: {total_marks}/{max_marks}")
print(f"Percentage : {percentage:.2f}%")

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade      : {grade}")

# Example:
# Total marks: 420, Subjects: 5 -> 84.0% -> Grade B
