# Question:
# Take a number from the user.
# Print 'Divisible by 7' if the number is divisible by 7,
# otherwise print 'Not Divisible by 7'.
#
# Example:
#   Input: 49  -> Output: Divisible by 7
#   Input: 10  -> Output: Not Divisible by 7

number = int(input("Enter a number: "))

if number % 7 == 0:
    print("Divisible by 7")
else:
    print("Not Divisible by 7")
