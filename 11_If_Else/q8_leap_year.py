# Question:
# Take a year from the user.
# Print 'Leap Year' if it is a leap year, otherwise print 'Not Leap Year'.
#
# A year is a leap year if:
#   - Divisible by 4 AND not divisible by 100
#   - OR divisible by 400
#
# Example:
#   Input: 2000  -> Output: Leap Year
#   Input: 1900  -> Output: Not Leap Year
#   Input: 2024  -> Output: Leap Year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")
