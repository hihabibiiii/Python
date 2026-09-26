# Question 12 (Hard):
# Compute compound interest.
# Formula: A = P * (1 + r/n) ** (n*t)
#   P = principal amount
#   r = annual interest rate (as decimal, e.g. 0.05 for 5%)
#   n = number of times interest is compounded per year
#   t = time in years
# Take all values from the user and print the final amount and interest earned.

# Solution:
P = float(input("Principal amount (P): "))
r = float(input("Annual interest rate (e.g. 0.05 for 5%): "))
n = float(input("Compounding frequency per year (n): "))
t = float(input("Time in years (t): "))

A = P * (1 + r / n) ** (n * t)
interest = A - P

print(f"\nFinal amount (A)  : ${A:.2f}")
print(f"Interest earned   : ${interest:.2f}")

# Example:
# P=1000, r=0.05, n=12, t=5
# Final amount (A)  : $1283.36
# Interest earned   : $283.36
