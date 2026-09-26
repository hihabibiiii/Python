# Question 5 (Easy):
# Use isinstance() to check if a value belongs to a specific type.
# Test each of the following:
#   - 42   -> is it an int?
#   - 3.14 -> is it a float?
#   - "hi" -> is it a str?
# Print the result of each check.

# Solution:
print(isinstance(42, int))       # Should be True
print(isinstance(3.14, float))   # Should be True
print(isinstance("hi", str))     # Should be True

# Extra checks to show False results:
print(isinstance(42, str))       # False - 42 is not a string
print(isinstance("hi", int))     # False - "hi" is not an int

# Output:
# True
# True
# True
# False
# False
