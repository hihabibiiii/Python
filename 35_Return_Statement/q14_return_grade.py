# Question 14 (Hard):
# Define a function called get_grade that takes a mark (0-100)
# and returns the letter grade. Use return inside if/elif/else.
# Grading: 90+=A, 80+=B, 70+=C, 60+=D, below 60=F

# Solution:
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

# Test with sample marks
marks = [95, 83, 72, 61, 55, 100, 0, 88]
print(f"{'Mark':<8} {'Grade'}")
print("-" * 15)
for m in marks:
    print(f"{m:<8} {get_grade(m)}")

# Get mark from user
mark = int(input("\nEnter a mark (0-100): "))
if 0 <= mark <= 100:
    grade = get_grade(mark)
    print(f"Grade for {mark}: {grade}")
else:
    print("Invalid mark. Please enter a value between 0 and 100.")

# Example Input:  78
# Example Output: Grade for 78: C
