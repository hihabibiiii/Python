# Question:
# Take a student's mark from the user.
# If mark >= 50:
#   - Check if mark >= 75:
#     - Yes -> print 'Distinction'
#     - No  -> print 'Pass'
# If mark < 50:
#   - Print 'Fail'
#
# Example:
#   Input: 80  -> Output: Distinction
#   Input: 60  -> Output: Pass
#   Input: 40  -> Output: Fail

mark = float(input("Enter the student's mark (0-100): "))

if mark >= 50:
    if mark >= 75:
        print("Result: Distinction")
    else:
        print("Result: Pass")
else:
    print("Result: Fail")
