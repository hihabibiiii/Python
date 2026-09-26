# Question: Print today's date using datetime.date.today().
# Display the date in multiple formats.

# Example output:
# Today's date: 2024-01-15
# Day: 15
# Month: 1
# Year: 2024

import datetime

today = datetime.date.today()

print(f"Today's date: {today}")
print(f"Day:   {today.day}")
print(f"Month: {today.month}")
print(f"Year:  {today.year}")
print(f"Type:  {type(today)}")
