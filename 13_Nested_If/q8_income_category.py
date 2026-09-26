# Question:
# Take a person's annual income from the user.
# If income > 50,000:
#   - If income > 100,000: print 'Rich'
#   - Else: print 'Comfortable'
# If income <= 50,000:
#   - If income > 20,000: print 'Middle class'
#   - Else: print 'Below poverty line'
#
# Example:
#   Input: 150000  -> Rich
#   Input: 75000   -> Comfortable
#   Input: 35000   -> Middle class
#   Input: 15000   -> Below poverty line

income = float(input("Enter annual income: "))

if income > 50000:
    if income > 100000:
        print("Income Category: Rich")
    else:
        print("Income Category: Comfortable")
else:
    if income > 20000:
        print("Income Category: Middle class")
    else:
        print("Income Category: Below poverty line")
