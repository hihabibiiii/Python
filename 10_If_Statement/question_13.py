# Question:
# Take a year from the user.
# If it is a leap year (divisible by 4 AND (not by 100 OR divisible by 400)),
# print "Leap Year".

# Example:
# Enter a year: 2024
# Leap Year

year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap Year")
