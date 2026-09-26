# Question: Print the current date AND time using datetime.datetime.now().
# Show individual components: year, month, day, hour, minute, second.

# Example output:
# Current date and time: 2024-01-15 10:30:45.123456
# Year:   2024
# Month:  1
# Day:    15
# Hour:   10
# Minute: 30
# Second: 45

import datetime

now = datetime.datetime.now()

print(f"Current date and time: {now}")
print(f"Year:        {now.year}")
print(f"Month:       {now.month}")
print(f"Day:         {now.day}")
print(f"Hour:        {now.hour}")
print(f"Minute:      {now.minute}")
print(f"Second:      {now.second}")
print(f"Microsecond: {now.microsecond}")
print(f"\nDate part only: {now.date()}")
print(f"Time part only: {now.time()}")
