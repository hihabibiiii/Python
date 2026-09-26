# Question 8 (Medium):
# Take a year from the user.
# Check if it is a leap year using comparison and modulo operators.
# A year is a leap year if:
#   - divisible by 4 AND not by 100, OR
#   - divisible by 400

# Solution:
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a LEAP year.")
else:
    print(f"{year} is NOT a leap year.")

# Example:
# 2000 -> Leap year (divisible by 400)
# 1900 -> Not a leap year (divisible by 100 but not 400)
# 2024 -> Leap year (divisible by 4, not by 100)
