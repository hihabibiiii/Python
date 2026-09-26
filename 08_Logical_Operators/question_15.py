# Question:
# Take marks for 5 subjects from the user.
# A student has passed if ALL five marks are >= 40.
# Use a single combined `and` condition across all five subjects.

# Example:
# Enter mark 1: 65
# Enter mark 2: 72
# Enter mark 3: 48
# Enter mark 4: 39
# Enter mark 5: 80
# Result: Failed

m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))
m4 = int(input("Enter mark 4: "))
m5 = int(input("Enter mark 5: "))

if m1 >= 40 and m2 >= 40 and m3 >= 40 and m4 >= 40 and m5 >= 40:
    avg = (m1 + m2 + m3 + m4 + m5) / 5
    print(f"Result: Passed! Average: {avg:.2f}")
else:
    print("Result: Failed (one or more subjects below 40).")
