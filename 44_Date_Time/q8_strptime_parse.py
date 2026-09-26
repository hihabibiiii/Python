# Question: Parse a date string '2024-01-15' into a date object using strptime().
# strptime = "string parse time" — converts a string to a datetime object.

# Example output:
# Date string: '2024-01-15'
# Parsed datetime object: 2024-01-15 00:00:00
# Type: <class 'datetime.datetime'>
# Year: 2024, Month: 1, Day: 15
# Formatted back: Monday, 15 January 2024

import datetime

# Parse a hardcoded date string
date_string = '2024-01-15'
parsed_date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

print(f"Date string: '{date_string}'")
print(f"Parsed datetime object: {parsed_date}")
print(f"Type: {type(parsed_date)}")
print(f"Year: {parsed_date.year}, Month: {parsed_date.month}, Day: {parsed_date.day}")
print(f"Formatted back: {parsed_date.strftime('%A, %d %B %Y')}")

# Parse different format strings
print("\n--- Parsing different formats ---")
date1 = datetime.datetime.strptime("15/01/2024", "%d/%m/%Y")
date2 = datetime.datetime.strptime("Jan 15, 2024", "%b %d, %Y")
date3 = datetime.datetime.strptime("2024-01-15 10:30:00", "%Y-%m-%d %H:%M:%S")

print(f"'15/01/2024' → {date1.date()}")
print(f"'Jan 15, 2024' → {date2.date()}")
print(f"'2024-01-15 10:30:00' → {date3}")

# User input
print()
user_str = input("Enter a date (YYYY-MM-DD): ")
try:
    user_date = datetime.datetime.strptime(user_str, '%Y-%m-%d')
    print(f"Parsed: {user_date.strftime('%A, %B %d, %Y')}")
except ValueError:
    print("Invalid format! Please use YYYY-MM-DD (e.g., 2024-01-15)")
