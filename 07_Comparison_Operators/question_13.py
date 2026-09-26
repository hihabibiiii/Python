# Question 13 (Hard):
# Take two dates as day/month/year integers from the user.
# Compare which date comes first using comparison operators.

# Solution:
print("--- Date 1 ---")
day1   = int(input("Day   (1-31): "))
month1 = int(input("Month (1-12): "))
year1  = int(input("Year       : "))

print("--- Date 2 ---")
day2   = int(input("Day   (1-31): "))
month2 = int(input("Month (1-12): "))
year2  = int(input("Year       : "))

date1_str = f"{day1:02d}/{month1:02d}/{year1}"
date2_str = f"{day2:02d}/{month2:02d}/{year2}"

if year1 < year2:
    print(f"\n{date1_str} comes BEFORE {date2_str}")
elif year1 > year2:
    print(f"\n{date2_str} comes BEFORE {date1_str}")
elif month1 < month2:
    print(f"\n{date1_str} comes BEFORE {date2_str}")
elif month1 > month2:
    print(f"\n{date2_str} comes BEFORE {date1_str}")
elif day1 < day2:
    print(f"\n{date1_str} comes BEFORE {date2_str}")
elif day1 > day2:
    print(f"\n{date2_str} comes BEFORE {date1_str}")
else:
    print(f"\nBoth dates are the same: {date1_str}")

# Example:
# Date1: 15/03/2023 vs Date2: 20/01/2024 -> Date1 comes before
