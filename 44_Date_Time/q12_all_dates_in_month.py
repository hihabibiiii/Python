# Question: Print all dates in a given month using a timedelta loop.
# Ask the user for a year and month, then print every date in that month.

# Example output:
# Enter year: 2024
# Enter month (1-12): 2
# 
# All dates in February 2024:
# Thu, Feb 01, 2024
# Fri, Feb 02, 2024
# ...
# Thu, Feb 29, 2024
# Total days: 29

import datetime
import calendar

print("List All Dates in a Month")
print("-" * 30)

try:
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))

    # Get number of days in the month
    _, days_in_month = calendar.monthrange(year, month)

    # Start from the 1st of the month
    current_date = datetime.date(year, month, 1)
    end_date = datetime.date(year, month, days_in_month)

    month_name = datetime.date(year, month, 1).strftime('%B')
    print(f"\nAll dates in {month_name} {year}:")
    print("-" * 25)

    # Loop through all dates using timedelta
    while current_date <= end_date:
        print(current_date.strftime("%a, %b %d, %Y"))
        current_date += datetime.timedelta(days=1)

    print("-" * 25)
    print(f"Total days: {days_in_month}")

except ValueError as e:
    print(f"Invalid input: {e}")
