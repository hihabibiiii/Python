# Question:
# Start with a variable n = 500.
# Use //= to keep dividing n by 3 (floor division) until it is less than 10.
# Print n after each step.

# Example Output:
# n = 500
# n = 166
# n = 55
# n = 18
# n = 6  -> Less than 10, stop.

n = 500
print(f"n = {n}")
while n >= 10:
    n //= 3
    print(f"n = {n}")
print("n is now less than 10. Done.")
