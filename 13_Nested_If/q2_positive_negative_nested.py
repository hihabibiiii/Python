# Question:
# Take a number from the user.
# If the number is positive:
#   - Check if it's even or odd and print accordingly.
# If the number is negative:
#   - Check if it's less than -100 and print 'Very large negative' or 'Moderately negative'.
#
# Example:
#   Input: 8    -> Output: Positive and Even
#   Input: 7    -> Output: Positive and Odd
#   Input: -150 -> Output: Negative and very large (below -100)
#   Input: -50  -> Output: Negative and moderately negative

number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    if number < -100:
        print("Negative and very large (below -100)")
    else:
        print("Negative and moderately negative")
