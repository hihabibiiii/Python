# Question: Create a list of numbers and compute their sum WITHOUT using the built-in sum().
# Use a loop to add up all elements manually.
# Example:
#   List: [10, 20, 30, 40, 50]
#   Sum:  150

numbers = [10, 20, 30, 40, 50]
print("Numbers:", numbers)

total = 0
for num in numbers:
    total = total + num

print("Sum (without using sum()):", total)
