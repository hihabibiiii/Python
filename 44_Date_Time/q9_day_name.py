# Question: Print the day name (Monday, Tuesday, etc.) of a given date.
# Ask the user for a date and display the day of the week.

# Example output:
# Enter year: 2024
# Enter month: 1
# Enter day: 15
# The date 2024-01-15 is a Monday.
# Day number (0=Monday, 6=Sunday): 0
# ISO day number (1=Monday, 7=Sunday): 1

import datetime

print("Find the Day of the Week")
print("-" * 30)

try:
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

    date = datetime.date(year, month, day)

    # strftime('%A') returns full day name
    day_name = date.strftime('%A')
    print(f"\nThe date {date} is a {day_name}.")
    print(f"Day number (0=Monday, 6=Sunday): {date.weekday()}")
    print(f"ISO day number (1=Monday, 7=Sunday): {date.isoweekday()}")

    # Show the whole week
    print(f"\nThe week containing {date}:")
    # Find Monday of that week
    monday = date - datetime.timedelta(days=date.weekday())
    for i in range(7):
        day_in_week = monday + datetime.timedelta(days=i)
        marker = " ← selected" if day_in_week == date else ""
        print(f"  {day_in_week.strftime('%A')}: {day_in_week}{marker}")

except ValueError as e:
    print(f"Invalid date: {e}")
