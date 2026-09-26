# Question:
# Check voting eligibility using nested if.
# Step 1: If age >= 18 (eligible by age):
#   Step 2: If is_citizen == 'yes' (citizen check):
#     Step 3: If is_registered == 'yes': print 'You can vote!'
#             Else: print 'You are not registered to vote.'
#   Else (not a citizen): print 'Non-citizens cannot vote.'
# Else (too young): print 'You must be at least 18 to vote.'
#
# Example:
#   age=20, citizen=yes, registered=yes -> You can vote!
#   age=20, citizen=yes, registered=no  -> You are not registered to vote.
#   age=20, citizen=no                  -> Non-citizens cannot vote.
#   age=16                              -> You must be at least 18 to vote.

age = int(input("Enter your age: "))

if age >= 18:
    is_citizen = input("Are you a citizen? (yes/no): ").lower()
    if is_citizen == "yes":
        is_registered = input("Are you registered to vote? (yes/no): ").lower()
        if is_registered == "yes":
            print("You can vote!")
        else:
            print("You are not registered to vote.")
    else:
        print("Non-citizens cannot vote.")
else:
    print("You must be at least 18 to vote.")
