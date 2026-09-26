# Question 4 (Easy):
# Define a function called min_max that takes a list of numbers
# and returns BOTH the minimum and maximum values as a tuple.
# Unpack the returned tuple when calling.

# Solution:
def min_max(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    return minimum, maximum  # returns a tuple

nums = [3, 1, 9, 2, 7, 5, 8, 4, 6]
print("List:", nums)

lo, hi = min_max(nums)
print(f"Minimum: {lo}")
print(f"Maximum: {hi}")

# Another example
raw = input("\nEnter numbers separated by spaces: ")
user_nums = [float(x) for x in raw.split()]
lo2, hi2 = min_max(user_nums)
print(f"Min: {lo2}, Max: {hi2}")

# Example Input:  10 -5 3 22 7
# Example Output: Min: -5.0, Max: 22.0
