# Question:
# Take the user's age as input.
# Print 'Adult' if age >= 18, otherwise print 'Minor'.
#
# Example:
#   Input: 20  -> Output: Adult
#   Input: 15  -> Output: Minor

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
