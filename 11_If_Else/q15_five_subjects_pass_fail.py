# Question:
# Take marks of 5 subjects from the user.
# Compute the average.
# Print 'Passed' if:
#   - The average is >= 50, AND
#   - No subject has a mark below 30
# Otherwise print 'Failed' and explain the reason.
#
# Example:
#   Marks: 60, 55, 70, 65, 80  -> Average=66, Passed
#   Marks: 60, 55, 25, 65, 80  -> Failed (Subject 3 is below 30)
#   Marks: 40, 35, 30, 35, 40  -> Average=36, Failed (Average below 50)

print("Enter marks for 5 subjects:")
mark1 = float(input("Subject 1: "))
mark2 = float(input("Subject 2: "))
mark3 = float(input("Subject 3: "))
mark4 = float(input("Subject 4: "))
mark5 = float(input("Subject 5: "))

average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5
print(f"\nAverage Mark: {average:.2f}")

# Check if any subject is below 30
below_30 = False
if mark1 < 30 or mark2 < 30 or mark3 < 30 or mark4 < 30 or mark5 < 30:
    below_30 = True

if average >= 50 and not below_30:
    print("Result: Passed")
else:
    print("Result: Failed")
    if average < 50:
        print("Reason: Average mark is below 50.")
    if below_30:
        print("Reason: One or more subjects have a mark below 30.")
