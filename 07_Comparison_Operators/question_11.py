# Question 11 (Hard):
# Take marks for 5 subjects from the user.
# Compare each mark to 50 (passing mark).
# Count how many subjects are passing (without using functions or lists).

# Solution:
mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))
mark4 = float(input("Enter mark for Subject 4: "))
mark5 = float(input("Enter mark for Subject 5: "))

pass_count = 0

if mark1 >= 50:
    pass_count = pass_count + 1
if mark2 >= 50:
    pass_count = pass_count + 1
if mark3 >= 50:
    pass_count = pass_count + 1
if mark4 >= 50:
    pass_count = pass_count + 1
if mark5 >= 50:
    pass_count = pass_count + 1

print(f"\nMarks  : {mark1}, {mark2}, {mark3}, {mark4}, {mark5}")
print(f"Passed : {pass_count} out of 5 subjects")
print(f"Failed : {5 - pass_count} subject(s)")

# Example:
# Marks: 60, 45, 75, 40, 80 -> Passed: 3
