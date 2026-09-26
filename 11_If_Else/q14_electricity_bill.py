# Question:
# Calculate electricity bill based on units consumed.
# Pricing (if/else only, 2 main branches):
#   - Up to 100 units:        1.5 per unit
#   - 101 to 300 units:       3.0 per unit
#   - Above 300 units:        5.0 per unit
# Take the number of units from the user and print the total bill.
#
# Example:
#   Input: 80   -> Output: Bill = 120.0
#   Input: 200  -> Output: Bill = 600.0
#   Input: 350  -> Output: Bill = 1750.0

units = float(input("Enter the number of units consumed: "))

if units <= 100:
    bill = units * 1.5
else:
    if units <= 300:
        bill = units * 3.0
    else:
        bill = units * 5.0

print(f"Total Electricity Bill: {bill:.2f}")
