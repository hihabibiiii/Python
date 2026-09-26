# Question:
# Take a student's mark from the user.
# Print the letter grade based on these rules:
#   A  -> mark >= 90
#   B  -> mark >= 75
#   C  -> mark >= 60
#   D  -> mark >= 50
#   F  -> mark < 50
#
# Example:
#   Input: 95  -> Output: Grade: A
#   Input: 80  -> Output: Grade: B
#   Input: 45  -> Output: Grade: F

mark = float(input("Enter the student's mark (0-100): "))

if mark >= 90:
    grade = "A"
elif mark >= 75:
    grade = "B"
elif mark >= 60:
    grade = "C"
elif mark >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
