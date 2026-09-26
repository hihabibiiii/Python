# Question 15 (Hard):
# Demonstrate short-circuit evaluation in Python.
# In 'and', if the first condition is False, the second is NOT evaluated.
# In 'or', if the first condition is True, the second is NOT evaluated.
# Show this by creating a case where the second expression would cause a
# ZeroDivisionError but doesn't execute due to short-circuiting.

# Solution:

# --- AND short-circuit (first is False, so second is skipped) ---
x = 0
print("Testing AND short-circuit:")
print("x =", x)
# If x != 0 is False, Python skips the right side entirely.
result = (x != 0) and (10 / x > 1)   # 10/x would crash if x==0, but it's skipped
print("(x != 0) and (10 / x > 1) =", result)

# --- OR short-circuit (first is True, so second is skipped) ---
print("\nTesting OR short-circuit:")
y = 5
print("y =", y)
# Since y > 0 is True, the second part is skipped.
result2 = (y > 0) or (10 / 0 > 1)   # 10/0 would crash, but it's skipped
print("(y > 0) or (10 / 0 > 1)  =", result2)

print("\nNo crash occurred — thanks to short-circuit evaluation!")

# Output:
# Testing AND short-circuit:
# x = 0
# (x != 0) and (10 / x > 1) = False
#
# Testing OR short-circuit:
# y = 5
# (y > 0) or (10 / 0 > 1)  = True
#
# No crash occurred — thanks to short-circuit evaluation!
