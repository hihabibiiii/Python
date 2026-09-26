# Question:
# Calculate electricity bill based on units consumed.
# Pricing tiers:
#   0 - 100 units   : 2 per unit
#   101 - 200 units : 3 per unit
#   201 - 300 units : 4 per unit
#   > 300 units     : 5 per unit
#
# Take units from the user and print the total bill.
#
# Example:
#   Input: 80   -> Output: Bill = 160.0
#   Input: 150  -> Output: Bill = 450.0
#   Input: 250  -> Output: Bill = 1000.0
#   Input: 400  -> Output: Bill = 2000.0

units = float(input("Enter the number of units consumed: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
elif units <= 300:
    bill = units * 4
else:
    bill = units * 5

print(f"Total Electricity Bill: {bill:.2f}")
