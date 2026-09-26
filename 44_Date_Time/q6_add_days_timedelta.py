# Question: Add 30 days to today's date using timedelta.
# Also compute dates for next week, next month, and next year.

# Example output:
# Today:          2024-01-15
# In 7 days:      2024-01-22
# In 30 days:     2024-02-14
# In 100 days:    2024-04-25
# 30 days ago:    2023-12-16

import datetime

today = datetime.date.today()

# timedelta represents a duration (number of days)
week = datetime.timedelta(days=7)
month = datetime.timedelta(days=30)
hundred_days = datetime.timedelta(days=100)

print(f"Today:          {today}")
print(f"In 7 days:      {today + week}")
print(f"In 30 days:     {today + month}")
print(f"In 100 days:    {today + hundred_days}")
print(f"30 days ago:    {today - month}")

# User input: add custom days
days = int(input("\nHow many days to add to today? "))
future_date = today + datetime.timedelta(days=days)
print(f"Today + {days} days = {future_date}")
print(f"Formatted: {future_date.strftime('%A, %B %d, %Y')}")
