# Question:
# Calculate income tax based on annual income.
# Tax slabs:
#   Income < 250,000          : 0% tax
#   250,001 to 500,000        : 5% tax
#   500,001 to 1,000,000      : 20% tax
#   Above 1,000,000           : 30% tax
#
# Take the annual income from the user and print the tax amount and net income.
#
# Example:
#   Input: 200000   -> Tax = 0, Net Income = 200000
#   Input: 400000   -> Tax = 20000, Net Income = 380000
#   Input: 750000   -> Tax = 150000, Net Income = 600000
#   Input: 1500000  -> Tax = 450000, Net Income = 1050000

income = float(input("Enter your annual income: "))

if income <= 250000:
    tax_rate = 0
elif income <= 500000:
    tax_rate = 5
elif income <= 1000000:
    tax_rate = 20
else:
    tax_rate = 30

tax = income * tax_rate / 100
net_income = income - tax

print(f"\nAnnual Income : {income:.2f}")
print(f"Tax Rate      : {tax_rate}%")
print(f"Tax Amount    : {tax:.2f}")
print(f"Net Income    : {net_income:.2f}")
