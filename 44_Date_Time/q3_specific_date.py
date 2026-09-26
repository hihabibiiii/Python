# Question: Create a specific date object using datetime.date(year, month, day).
# Ask the user to enter a year, month, and day, then create and display the date.

# Example output:
# Enter year: 2000
# Enter month: 6
# Enter day: 15
# Date created: 2000-06-15
# This is a valid date object!
# Formatted: June 15, 2000

import datetime

print("Create a specific date object")
print("-" * 30)

try:
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

    specific_date = datetime.date(year, month, day)
    print(f"\nDate created: {specific_date}")
    print(f"This is a valid date object!")
    print(f"Type: {type(specific_date)}")
    print(f"Formatted: {specific_date.strftime('%B %d, %Y')}")

except ValueError as e:
    print(f"Invalid date: {e}")
