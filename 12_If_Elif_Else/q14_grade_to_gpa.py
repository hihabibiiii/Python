# Question:
# Take a letter grade (A, B, C, D, or F) from the user.
# Print the corresponding GPA value and status.
#   A  -> GPA 4.0, Excellent
#   B  -> GPA 3.0, Good
#   C  -> GPA 2.0, Average
#   D  -> GPA 1.0, Below Average
#   F  -> GPA 0.0, Fail
#
# Example:
#   Input: A  -> Output: GPA: 4.0 | Status: Excellent
#   Input: C  -> Output: GPA: 2.0 | Status: Average
#   Input: F  -> Output: GPA: 0.0 | Status: Fail

grade = input("Enter your letter grade (A/B/C/D/F): ").upper()

if grade == "A":
    gpa = 4.0
    status = "Excellent"
elif grade == "B":
    gpa = 3.0
    status = "Good"
elif grade == "C":
    gpa = 2.0
    status = "Average"
elif grade == "D":
    gpa = 1.0
    status = "Below Average"
elif grade == "F":
    gpa = 0.0
    status = "Fail"
else:
    gpa = None
    status = None

if status is not None:
    print(f"GPA: {gpa} | Status: {status}")
else:
    print(f"Invalid grade '{grade}'. Please enter A, B, C, D, or F.")
