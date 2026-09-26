# Question:
# Simulate a loan approval system using nested if.
# Step 1: If credit_score >= 700 (creditworthy):
#   Step 2: If income >= 30,000 (sufficient income):
#     Step 3: If existing_loans == 0 (no existing loans):
#               print 'Loan Approved!'
#             Else: print 'Cannot approve: You already have existing loans.'
#     Else: print 'Income too low. Minimum income required: 30,000.'
#   Else: print 'Credit score too low. Minimum score required: 700.'
#
# Example:
#   score=750, income=40000, loans=0  -> Loan Approved!
#   score=750, income=40000, loans=2  -> Cannot approve: existing loans
#   score=750, income=20000           -> Income too low
#   score=600                          -> Credit score too low

credit_score = int(input("Enter your credit score (300-850): "))

if credit_score >= 700:
    income = float(input("Enter your annual income: "))
    if income >= 30000:
        existing_loans = int(input("Enter number of existing loans: "))
        if existing_loans == 0:
            print("Loan Approved!")
        else:
            print("Cannot approve: You already have existing loans.")
    else:
        print("Income too low. Minimum annual income required: 30,000.")
else:
    print("Credit score too low. Minimum credit score required: 700.")
