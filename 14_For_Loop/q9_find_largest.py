# Question:
# Find the largest number in the following list using a for loop.
# Do NOT use the built-in max() function.
#
# numbers = [34, 7, 23, 32, 5, 62, 15, 89, 21]
#
# Expected Output:
#   The largest number is: 89

numbers = [34, 7, 23, 32, 5, 62, 15, 89, 21]

largest = numbers[0]  # Assume the first element is the largest
for num in numbers:
    if num > largest:
        largest = num

print(f"List: {numbers}")
print(f"The largest number is: {largest}")
