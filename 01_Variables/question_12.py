# Question 12 (Hard):
# Start with a variable `value = 20`.
# Apply augmented assignment operators in this order:
#   1. Add 10 using +=
#   2. Subtract 5 using -=
#   3. Multiply by 3 using *=
#   4. Divide by 5 using /=
# Print the value after each step with a label.

# Solution:
value = 20
print("Initial value:", value)

value += 10
print("After += 10:", value)

value -= 5
print("After -= 5:", value)

value *= 3
print("After *= 3:", value)

value /= 5
print("After /= 5:", value)

# Output:
# Initial value: 20
# After += 10: 30
# After -= 5: 25
# After *= 3: 75
# After /= 5: 15.0
