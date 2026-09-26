# Question:
# Take a student's mark from the user.
# Print 'Pass' if the mark is 50 or above, otherwise print 'Fail'.
#
# Example:
#   Input: 75  -> Output: Pass
#   Input: 40  -> Output: Fail

mark = float(input("Enter the student's mark: "))

if mark >= 50:
    print("Pass")
else:
    print("Fail")
