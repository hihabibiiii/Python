# Question: Import the datetime module and print today's date in various formats.

# Example output:
# === Datetime Module Demo ===
# Today's date: 2024-01-15
# Formatted: Monday, 15 January 2024
# Day: 15
# Month: 1
# Year: 2024
# Current date & time: 2024-01-15 10:30:45.123456

import datetime

print("=" * 35)
print("     Datetime Module Demo")
print("=" * 35)

# Get today's date
today = datetime.date.today()
print(f"Today's date: {today}")
print(f"Formatted: {today.strftime('%A, %d %B %Y')}")
print(f"Day: {today.day}")
print(f"Month: {today.month}")
print(f"Year: {today.year}")

# Current date and time
now = datetime.datetime.now()
print(f"\nCurrent date & time: {now}")
print(f"Time only: {now.strftime('%H:%M:%S')}")
print(f"12-hour format: {now.strftime('%I:%M %p')}")
