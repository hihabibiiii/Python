# Question 12 (Hard):
# Demonstrate type coercion (implicit and explicit type mixing):
#   1. Add an int and a float — result becomes float.
#   2. Multiply a string by an int — string repeats.
#   3. Use a bool in arithmetic — True acts as 1, False as 0.
# Print each result with a label.

# Solution:
# 1. int + float -> float
result1 = 5 + 2.0
print("int + float:", result1, "| Type:", type(result1))

# 2. str * int -> repeated string
result2 = "ha" * 3
print("str * int:", result2, "| Type:", type(result2))

# 3. bool in arithmetic
result3 = True + 9
result4 = False * 100
print("True + 9:", result3)
print("False * 100:", result4)

# Output:
# int + float: 7.0 | Type: <class 'float'>
# str * int: hahaha | Type: <class 'str'>
# True + 9: 10
# False * 100: 0
