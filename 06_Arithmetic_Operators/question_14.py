# Question 14 (Hard):
# Given a 4-digit number, compute the sum of its digits
# using ONLY arithmetic operators (//, %) — no loops, no str().

# Solution:
number = int(input("Enter a 4-digit number: "))

thousands = number // 1000
hundreds  = (number % 1000) // 100
tens      = (number % 100) // 10
ones      = number % 10

digit_sum = thousands + hundreds + tens + ones

print(f"Number       : {number}")
print(f"Digits       : {thousands} + {hundreds} + {tens} + {ones}")
print(f"Sum of digits: {digit_sum}")

# Example:
# Enter a 4-digit number: 1234
# Number       : 1234
# Digits       : 1 + 2 + 3 + 4
# Sum of digits: 10
