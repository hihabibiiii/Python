# Question:
# Take two numbers from the user.
# If the first number is positive (> 0):
#   - Check if the second is also positive -> print 'Both positive'
#   - Else print 'First positive, second non-positive'
# If the first number is NOT positive (<= 0):
#   - Check if the second is also non-positive -> print 'Both negative or zero'
#   - Else print 'First non-positive, second positive'
#
# Example:
#   Input: 5, 3    -> Both positive
#   Input: 5, -2   -> First positive, second non-positive
#   Input: -4, -1  -> Both negative or zero
#   Input: -4, 3   -> First non-positive, second positive

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > 0:
    if num2 > 0:
        print("Both positive")
    else:
        print("First positive, second non-positive")
else:
    if num2 <= 0:
        print("Both negative or zero")
    else:
        print("First non-positive, second positive")
