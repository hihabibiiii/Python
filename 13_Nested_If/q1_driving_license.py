# Question:
# Take a person's age from the user.
# If age >= 18, check if age >= 21:
#   - age >= 21: print 'Full License - eligible for all vehicles'
#   - age >= 18 but < 21: print 'Learner License - limited privileges'
# If age < 18, print 'Not eligible for a driving license'.
#
# Example:
#   Input: 25  -> Output: Full License - eligible for all vehicles
#   Input: 19  -> Output: Learner License - limited privileges
#   Input: 16  -> Output: Not eligible for a driving license

age = int(input("Enter your age: "))

if age >= 18:
    if age >= 21:
        print("Full License - eligible for all vehicles")
    else:
        print("Learner License - limited privileges")
else:
    print("Not eligible for a driving license")
