# Question:
# Take a number from 1 to 7 representing a day of the week.
# (1=Monday, 2=Tuesday, ..., 5=Friday, 6=Saturday, 7=Sunday)
# If the day is a weekday (1 to 5), print "Weekday".

# Example:
# Enter day (1-7): 3
# Weekday

day = int(input("Enter day number (1=Mon ... 7=Sun): "))

if 1 <= day <= 5:
    print("Weekday")
