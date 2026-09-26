# Question:
# Take a year and a month (number 1-12) from the user.
# If year > 2000 (modern year):
#   - If month > 6: print 'Second half of a modern year'
#   - Else:         print 'First half of a modern year'
# If year <= 2000 (older year):
#   - If month > 6: print 'Second half of an older year'
#   - Else:         print 'First half of an older year'
#
# Example:
#   Input: year=2020, month=9  -> Second half of a modern year
#   Input: year=2020, month=3  -> First half of a modern year
#   Input: year=1990, month=10 -> Second half of an older year
#   Input: year=1990, month=2  -> First half of an older year

year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))

if year > 2000:
    if month > 6:
        print("Second half of a modern year (after 2000)")
    else:
        print("First half of a modern year (after 2000)")
else:
    if month > 6:
        print("Second half of an older year (up to 2000)")
    else:
        print("First half of an older year (up to 2000)")
