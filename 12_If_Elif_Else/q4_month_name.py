# Question:
# Take a number from 1 to 12 from the user.
# Print the corresponding month name.
#
# Example:
#   Input: 1   -> Output: January
#   Input: 6   -> Output: June
#   Input: 12  -> Output: December
#   Input: 13  -> Output: Invalid month number

number = int(input("Enter a month number (1-12): "))

if number == 1:
    print("January")
elif number == 2:
    print("February")
elif number == 3:
    print("March")
elif number == 4:
    print("April")
elif number == 5:
    print("May")
elif number == 6:
    print("June")
elif number == 7:
    print("July")
elif number == 8:
    print("August")
elif number == 9:
    print("September")
elif number == 10:
    print("October")
elif number == 11:
    print("November")
elif number == 12:
    print("December")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
