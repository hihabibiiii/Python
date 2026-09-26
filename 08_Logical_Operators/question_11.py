# Question:
# Take marks for three subjects from the user.
# A student passes only if ALL three marks are >= 40.
# Use `and` to check all conditions.

# Example:
# Enter marks for subject 1: 55
# Enter marks for subject 2: 42
# Enter marks for subject 3: 38
# Result: Failed (Subject 3 is below 40)

m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))

if m1 >= 40 and m2 >= 40 and m3 >= 40:
    print("Result: Passed all subjects!")
else:
    print("Result: Failed.")
    if m1 < 40:
        print("  Subject 1 is below 40.")
    if m2 < 40:
        print("  Subject 2 is below 40.")
    if m3 < 40:
        print("  Subject 3 is below 40.")
