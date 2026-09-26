# Question: Compute a person's age in years and remaining days from their birthdate to today.

# Example output:
# Enter your birth year: 1995
# Enter your birth month: 6
# Enter your birth day: 15
# 
# Your birthdate: June 15, 1995
# Today:          January 15, 2024
# 
# Age: 28 years and 214 days
# Next birthday: June 15, 2024 (152 days away)

import datetime

print("Age Calculator")
print("-" * 30)

try:
    year = int(input("Enter your birth year: "))
    month = int(input("Enter your birth month (1-12): "))
    day = int(input("Enter your birth day (1-31): "))

    birthdate = datetime.date(year, month, day)
    today = datetime.date.today()

    if birthdate > today:
        print("Error: Birthdate cannot be in the future!")
    else:
        print(f"\nYour birthdate: {birthdate.strftime('%B %d, %Y')}")
        print(f"Today:          {today.strftime('%B %d, %Y')}")

        # Calculate age in years
        age_years = today.year - birthdate.year
        # Check if birthday hasn't happened yet this year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age_years -= 1

        # Calculate last birthday
        try:
            last_birthday = datetime.date(today.year, birthdate.month, birthdate.day)
            if last_birthday > today:
                last_birthday = datetime.date(today.year - 1, birthdate.month, birthdate.day)
        except ValueError:
            # Handle Feb 29 birthdays
            last_birthday = datetime.date(today.year - 1, 2, 28)

        days_since_birthday = (today - last_birthday).days

        print(f"\nAge: {age_years} years and {days_since_birthday} days")

        # Next birthday
        try:
            next_birthday = datetime.date(today.year, birthdate.month, birthdate.day)
            if next_birthday <= today:
                next_birthday = datetime.date(today.year + 1, birthdate.month, birthdate.day)
        except ValueError:
            next_birthday = datetime.date(today.year + 1, 3, 1)  # Day after Feb 28

        days_until = (next_birthday - today).days
        print(f"Next birthday: {next_birthday.strftime('%B %d, %Y')} ({days_until} days away)")

except ValueError as e:
    print(f"Invalid date: {e}")
