# Question 7 (Medium):
# Take a total number of seconds from the user.
# Using // and %, compute and print the equivalent hours, minutes, and seconds.

# Solution:
total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds} seconds = {hours}h {minutes}m {seconds}s")

# Example:
# Enter total seconds: 3665
# 3665 seconds = 1h 1m 5s
