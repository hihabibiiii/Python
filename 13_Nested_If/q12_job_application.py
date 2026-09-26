# Question:
# Simulate a job application screening using nested if.
# Step 1: If age is between 18 and 60 (inclusive):
#   Step 2: If qualification == 'graduate':
#     Step 3: If experience >= 2 years:
#               print 'Application Approved!'
#             Else: print 'Need at least 2 years of experience.'
#     Else: print 'Graduate qualification required.'
# Else: print 'Age must be between 18 and 60.'
#
# Example:
#   age=25, graduate, 3 years  -> Application Approved!
#   age=25, graduate, 1 year   -> Need at least 2 years of experience.
#   age=25, diploma            -> Graduate qualification required.
#   age=17                     -> Age must be between 18 and 60.

age = int(input("Enter your age: "))

if 18 <= age <= 60:
    qualification = input("Enter your highest qualification (graduate/other): ").lower()
    if qualification == "graduate":
        experience = int(input("Enter years of work experience: "))
        if experience >= 2:
            print("Application Approved!")
        else:
            print("Need at least 2 years of experience.")
    else:
        print("Graduate qualification required.")
else:
    print("Age must be between 18 and 60.")
