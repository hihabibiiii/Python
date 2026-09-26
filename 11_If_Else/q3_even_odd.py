# Question:
# Take a number from the user.
# Print 'Even' if the number is divisible by 2, otherwise print 'Odd'.
#
# Example:
#   Input: 4   -> Output: Even
#   Input: 7   -> Output: Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
