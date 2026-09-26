# Question 7 (Medium):
# Given x = 10 and y = 20, swap the values of x and y WITHOUT using
# a third (temporary) variable.
# Print the values before and after the swap.

# Solution:
x = 10
y = 20
print("Before swap: x =", x, ", y =", y)

# Swap using Python tuple unpacking (no third variable needed)
x, y = y, x

print("After swap:  x =", x, ", y =", y)

# Output:
# Before swap: x = 10 , y = 20
# After swap:  x = 20 , y = 10
