# Question: Compute the difference between two dates in days.
# Ask the user for two dates, subtract them, and show the number of days between them.

# Example output:
# Enter first date:
#   Year: 2020
#   Month: 1
#   Day: 1
# Enter second date:
#   Year: 2024
#   Month: 1
#   Day: 15
# Difference: 1475 days

import datetime

print("Compute the number of days between two dates")
print("-" * 45)

try:
    print("Enter first date:")
    y1 = int(input("  Year: "))
    m1 = int(input("  Month: "))
    d1 = int(input("  Day: "))
    date1 = datetime.date(y1, m1, d1)

    print("Enter second date:")
    y2 = int(input("  Year: "))
    m2 = int(input("  Month: "))
    d2 = int(input("  Day: "))
    date2 = datetime.date(y2, m2, d2)

    # Subtraction returns a timedelta object
    difference = date2 - date1

    print(f"\nDate 1: {date1}")
    print(f"Date 2: {date2}")
    print(f"Difference: {abs(difference.days)} days")

    if difference.days > 0:
        print(f"Date 2 is {difference.days} days AFTER Date 1.")
    elif difference.days < 0:
        print(f"Date 2 is {abs(difference.days)} days BEFORE Date 1.")
    else:
        print("Both dates are the same!")

except ValueError as e:
    print(f"Invalid date: {e}")
