# Question 11 (Hard):
# Demonstrate operator precedence by computing the same numbers
# with different parentheses and showing the difference.

# Solution:
# Expression 1: default precedence (PEMDAS/BODMAS)
result1 = 2 + 3 * 4 - 1 / 2
print("2 + 3 * 4 - 1 / 2      =", result1)
# Evaluated as: 2 + (3*4) - (1/2) = 2 + 12 - 0.5 = 13.5

# Expression 2: with parentheses to change order
result2 = (2 + 3) * (4 - 1) / 2
print("(2 + 3) * (4 - 1) / 2  =", result2)
# Evaluated as: 5 * 3 / 2 = 15 / 2 = 7.5

result3 = 2 + 3 * (4 - 1 / 2)
print("2 + 3 * (4 - 1 / 2)    =", result3)
# Evaluated as: 2 + 3 * 3.5 = 2 + 10.5 = 12.5

print("\nSame numbers, different parentheses → different results!")

# Output:
# 2 + 3 * 4 - 1 / 2      = 13.5
# (2 + 3) * (4 - 1) / 2  = 7.5
# 2 + 3 * (4 - 1 / 2)    = 12.5
