# Question 12 (Hard):
# Define a function called smart_convert that takes a value
# and returns different types based on what the input looks like:
#   - If it's a digit string, return an int
#   - If it's a float string, return a float
#   - If it's "true" or "false" (case-insensitive), return a bool
#   - Otherwise return the string as-is

# Solution:
def smart_convert(value):
    # Check for boolean
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    # Check for integer
    if value.lstrip("-").isdigit():
        return int(value)
    # Check for float
    try:
        return float(value)
    except ValueError:
        pass
    # Default: return as string
    return value

# Test cases
test_values = ["42", "3.14", "True", "false", "hello", "-7", "2.0"]
print(f"{'Input':<12} {'Result':<12} {'Type'}")
print("-" * 40)
for v in test_values:
    result = smart_convert(v)
    print(f"{v:<12} {str(result):<12} {type(result).__name__}")

# Example Output:
# 42           42           int
# 3.14         3.14         float
# True         True         bool
# false        False        bool
# hello        hello        str
