# Question 7 (Medium):
# Take a total number of minutes from the user.
# Use floor division (//) to get hours, and modulo (%) to get remaining minutes.
# Print the result in hours and minutes.

# Solution:
total_minutes = int(input("Enter total minutes: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{total_minutes} minutes = {hours} hour(s) and {minutes} minute(s)")

# Example Input / Output:
# Enter total minutes: 135
# 135 minutes = 2 hour(s) and 15 minute(s)
