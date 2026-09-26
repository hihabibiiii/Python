# Question:
# Start with x = 100.
# Apply %= 7 three times and print the result after each step.
# This shows how modulo assignment changes the value.

# Example Output:
# After %=7 step 1: x = 2
# After %=7 step 2: x = 2
# After %=7 step 3: x = 2

x = 100
x %= 7
print(f"After %=7 step 1: x = {x}")
x %= 7
print(f"After %=7 step 2: x = {x}")
x %= 7
print(f"After %=7 step 3: x = {x}")
