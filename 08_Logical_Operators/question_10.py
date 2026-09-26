# Question:
# Take a year from the user and check if it is a leap year.
# A year is a leap year if:
#   - Divisible by 4 AND (NOT divisible by 100 OR divisible by 400).
# Use `and`, `or`, `not` operators.

# Example:
# Enter a year: 2000
# 2000 is a leap year.

year = int(input("Enter a year: "))

if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
