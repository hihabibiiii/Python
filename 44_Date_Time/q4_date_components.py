# Question: Get the year, month, and day from a date object.
# Create today's date and extract each component individually.

# Example output:
# Today's date object: 2024-01-15
# Extracting components:
# Year:  2024
# Month: 1  → January
# Day:   15

import datetime

# Create date object for today
today = datetime.date.today()

print(f"Today's date object: {today}")
print("Extracting components:")

year = today.year
month = today.month
day = today.day

print(f"Year:  {year}")
print(f"Month: {month}")
print(f"Day:   {day}")

# Month name lookup
month_names = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
print(f"\nMonth name: {month_names[month - 1]}")
print(f"Full formatted: {today.strftime('%A, %B %d, %Y')}")
