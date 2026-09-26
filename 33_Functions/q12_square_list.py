# Question 12 (Hard):
# Define a function called square_list that takes a list of numbers
# and returns a NEW list where each element is the square of the original.
# The original list should not be modified.

# Solution:
def square_list(numbers):
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared

# Test with examples
nums = [1, 2, 3, 4, 5]
result = square_list(nums)
print(f"Original: {nums}")
print(f"Squared:  {result}")

# With negative numbers and zeros
nums2 = [-3, -1, 0, 2, 4, 6]
print(f"\nOriginal: {nums2}")
print(f"Squared:  {square_list(nums2)}")

# Get numbers from user
raw = input("\nEnter numbers separated by spaces: ")
user_nums = [float(x) for x in raw.split()]
print(f"Squared: {square_list(user_nums)}")

# Example Input:  2 3 4 5
# Example Output: Squared: [4.0, 9.0, 16.0, 25.0]
