# Question: Check if a year is a leap year using the calendar module.
# Ask the user to enter a year and determine if it's a leap year.

# A leap year is:
# - Divisible by 4
# - EXCEPT centuries (divisible by 100) are NOT leap years
# - UNLESS also divisible by 400

# Example output:
# Enter a year: 2024
# 2024 IS a leap year! (February has 29 days)
# Days in February 2024: 29

# Enter a year: 1900
# 1900 is NOT a leap year. (divisible by 100 but not 400)

import calendar

year = int(input("Enter a year: "))

is_leap = calendar.isleap(year)

if is_leap:
    print(f"{year} IS a leap year! (February has 29 days)")
else:
    print(f"{year} is NOT a leap year. (February has 28 days)")

# Show days in each month for that year
print(f"\nCalendar for {year}:")
print(f"{'Month':<12} {'Days'}")
print("-" * 20)
for month_num in range(1, 13):
    month_name = calendar.month_name[month_num]
    days_in_month = calendar.monthrange(year, month_num)[1]
    print(f"{month_name:<12} {days_in_month}")

# Also list upcoming leap years
print(f"\nNext 5 leap years after {year}:")
count = 0
check = year + 1
while count < 5:
    if calendar.isleap(check):
        print(f"  {check}")
        count += 1
    check += 1
