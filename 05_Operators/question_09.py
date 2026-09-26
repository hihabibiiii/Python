# Question 9 (Medium):
# Start with a variable n = 100.
# Apply all augmented assignment operators step by step, printing after each.

# Solution:
n = 100
print("Initial n       =", n)

n += 20
print("After n += 20  :", n)

n -= 15
print("After n -= 15  :", n)

n *= 2
print("After n *= 2   :", n)

n /= 5
print("After n /= 5   :", n)

n //= 3
print("After n //= 3  :", n)

n **= 2
print("After n **= 2  :", n)

n %= 50
print("After n %= 50  :", n)

# Output:
# Initial n       = 100
# After n += 20  : 120
# After n -= 15  : 105
# After n *= 2   : 210
# After n /= 5   : 42.0
# After n //= 3  : 14.0
# After n **= 2  : 196.0
# After n %= 50  : 46.0
