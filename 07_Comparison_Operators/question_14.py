# Question 14 (Hard):
# Take marks for two students from the user.
# Compare them and print who scored higher and by how much.
# If equal, print that they scored the same.

# Solution:
name1 = input("Enter name of student 1: ")
mark1 = float(input(f"Enter {name1}'s mark: "))

name2 = input("Enter name of student 2: ")
mark2 = float(input(f"Enter {name2}'s mark: "))

print(f"\n{name1}: {mark1}")
print(f"{name2}: {mark2}")

if mark1 > mark2:
    diff = mark1 - mark2
    print(f"\n{name1} scored higher by {diff} marks.")
elif mark2 > mark1:
    diff = mark2 - mark1
    print(f"\n{name2} scored higher by {diff} marks.")
else:
    print(f"\nBoth scored the same: {mark1} marks.")

# Example:
# Alice: 85, Bob: 78 -> Alice scored higher by 7 marks.
