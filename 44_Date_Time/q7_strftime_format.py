# Question: Format a date using strftime() to produce 'DD-MM-YYYY' format.
# Also demonstrate other common date format strings.

# Example output:
# Today's date object: 2024-01-15
# 
# Format examples using strftime():
# DD-MM-YYYY:          15-01-2024
# MM/DD/YYYY:          01/15/2024
# Day Month Year:      15 January 2024
# Full:                Monday, 15 January 2024
# Short:               Mon, 15 Jan 2024
# US Format:           January 15, 2024

import datetime

today = datetime.date.today()
print(f"Today's date object: {today}")

print("\nFormat examples using strftime():")
print(f"DD-MM-YYYY:          {today.strftime('%d-%m-%Y')}")
print(f"MM/DD/YYYY:          {today.strftime('%m/%d/%Y')}")
print(f"Day Month Year:      {today.strftime('%d %B %Y')}")
print(f"Full:                {today.strftime('%A, %d %B %Y')}")
print(f"Short:               {today.strftime('%a, %d %b %Y')}")
print(f"US Format:           {today.strftime('%B %d, %Y')}")
print(f"ISO Format:          {today.strftime('%Y-%m-%d')}")

print("\n--- strftime format codes ---")
print("%d = day (01-31), %m = month (01-12), %Y = 4-digit year")
print("%A = full weekday, %B = full month name")
print("%H = hour (24h), %M = minute, %S = second")
