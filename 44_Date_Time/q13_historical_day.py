# Question: Find the day of the week for a historical date.
# Ask the user to enter any historical date and find out what day it was.

# Example output:
# === Historical Day Finder ===
# Enter year: 1969
# Enter month: 7
# Enter day: 20
# 
# July 20, 1969 was a SUNDAY.
# Fun fact: This was the day of the Apollo 11 Moon landing!

import datetime

print("=" * 35)
print("    Historical Day Finder")
print("=" * 35)

# Some famous dates for reference
famous_dates = {
    datetime.date(1969, 7, 20): "Apollo 11 Moon Landing",
    datetime.date(1945, 9, 2):  "End of World War II",
    datetime.date(2001, 9, 11): "9/11 Attacks",
    datetime.date(1989, 11, 9): "Berlin Wall fell",
    datetime.date(1776, 7, 4):  "US Independence Day",
}

try:
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

    target_date = datetime.date(year, month, day)
    day_name = target_date.strftime('%A').upper()
    formatted = target_date.strftime('%B %d, %Y')

    print(f"\n{formatted} was a {day_name}.")

    # Check if it's a famous date
    if target_date in famous_dates:
        print(f"Fun fact: {famous_dates[target_date]}!")

    today = datetime.date.today()
    if target_date < today:
        days_ago = (today - target_date).days
        print(f"This was {days_ago:,} days ago.")
    elif target_date > today:
        days_ahead = (target_date - today).days
        print(f"This is {days_ahead:,} days in the future.")
    else:
        print("This is today!")

except ValueError as e:
    print(f"Invalid date: {e}")
