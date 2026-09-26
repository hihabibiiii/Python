# Question 2 (Easy):
# Define a function called is_even that takes an integer
# and returns True if it is even, False otherwise.
# Print the result for several test cases.

# Solution:
def is_even(n):
    return n % 2 == 0

test_numbers = [0, 1, 2, 7, 10, -4, -3]
for num in test_numbers:
    result = is_even(num)
    print(f"is_even({num:>3}) = {result}")

# Get input from user
n = int(input("\nEnter an integer: "))
print(f"is_even({n}) = {is_even(n)}")

# Example Input:  6
# Example Output: is_even(6) = True
