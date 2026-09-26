# Question:
# Take a person's age from the user.
# Classify them into one of these categories:
#   Baby     -> 0-2 years
#   Toddler  -> 3-5 years
#   Child    -> 6-12 years
#   Teen     -> 13-19 years
#   Adult    -> 20-59 years
#   Senior   -> 60+ years
#
# Example:
#   Input: 1   -> Output: Baby
#   Input: 4   -> Output: Toddler
#   Input: 10  -> Output: Child
#   Input: 16  -> Output: Teen
#   Input: 35  -> Output: Adult
#   Input: 70  -> Output: Senior

age = int(input("Enter the person's age: "))

if age < 0:
    print("Invalid age! Age cannot be negative.")
elif age <= 2:
    print("Category: Baby")
elif age <= 5:
    print("Category: Toddler")
elif age <= 12:
    print("Category: Child")
elif age <= 19:
    print("Category: Teen")
elif age <= 59:
    print("Category: Adult")
else:
    print("Category: Senior")
