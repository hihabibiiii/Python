# Question:
# Take a number from 1 to 7 from the user.
# Print the corresponding day of the week.
#   1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday,
#   5 = Friday, 6 = Saturday, 7 = Sunday
#
# Example:
#   Input: 1  -> Output: Monday
#   Input: 5  -> Output: Friday
#   Input: 9  -> Output: Invalid number

number = int(input("Enter a number (1-7): "))

if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
else:
    print("Invalid number! Please enter a number between 1 and 7.")
