# Question:
# Take a month number (1-12) from the user.
# Print the number of days in that month.
# Assume February has 28 days (non-leap year).
#
# Example:
#   Input: 1   -> Output: January has 31 days
#   Input: 2   -> Output: February has 28 days
#   Input: 4   -> Output: April has 30 days
#   Input: 12  -> Output: December has 31 days

month = int(input("Enter a month number (1-12): "))

if month == 1:
    print("January has 31 days")
elif month == 2:
    print("February has 28 days")
elif month == 3:
    print("March has 31 days")
elif month == 4:
    print("April has 30 days")
elif month == 5:
    print("May has 31 days")
elif month == 6:
    print("June has 30 days")
elif month == 7:
    print("July has 31 days")
elif month == 8:
    print("August has 31 days")
elif month == 9:
    print("September has 30 days")
elif month == 10:
    print("October has 31 days")
elif month == 11:
    print("November has 30 days")
elif month == 12:
    print("December has 31 days")
else:
    print("Invalid month number!")
