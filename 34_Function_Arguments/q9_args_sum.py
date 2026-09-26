# Question 9 (Medium):
# Use *args to create a function that computes the sum of any number of numbers.
# The function should work with 2, 5, or 100 arguments.

# Solution:
def total_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum of 1, 2 =", total_sum(1, 2))
print("Sum of 1 to 5 =", total_sum(1, 2, 3, 4, 5))
print("Sum of 10, 20, 30, 40, 50 =", total_sum(10, 20, 30, 40, 50))
print("Sum of no numbers =", total_sum())

# Get numbers from user
raw = input("\nEnter numbers separated by spaces: ")
user_nums = [float(x) for x in raw.split()]
result = total_sum(*user_nums)
print(f"Sum of {user_nums} = {result}")

# Example Input:  3 7 2 10 1
# Example Output: Sum of [3.0, 7.0, 2.0, 10.0, 1.0] = 23.0
