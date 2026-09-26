# Question:
# Ask the user to enter a grade (A, B, or C).
# If the grade is "A", print "Excellent!".

# Example:
# Enter grade: A
# Excellent!

grade = input("Enter grade (A/B/C): ").strip().upper()

if grade == "A":
    print("Excellent!")
