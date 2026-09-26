# Question: Find the maximum and minimum values in a list WITHOUT using max() or min().
# Traverse the list, keeping track of the largest and smallest values seen.
# Example:
#   List: [34, 7, 23, 32, 5, 62]
#   Max: 62, Min: 5

numbers = [34, 7, 23, 32, 5, 62]
print("Numbers:", numbers)

current_max = numbers[0]
current_min = numbers[0]

for num in numbers:
    if num > current_max:
        current_max = num
    if num < current_min:
        current_min = num

print("Maximum (without max()):", current_max)
print("Minimum (without min()):", current_min)
