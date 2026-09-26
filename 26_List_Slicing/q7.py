# Question: Use step=-1 to reverse a specific portion of a list.
# Reverse only a middle sub-section, leaving the first and last elements in place.
# Example:
#   List: [1, 2, 3, 4, 5, 6, 7]
#   Reverse indices 2 to 5 (inclusive): [1, 2, 5, 4, 3, 6, 7]
#   Note: We extract the reversed slice and then reconstruct.

numbers = [1, 2, 3, 4, 5, 6, 7]
print("Original list:", numbers)

# Reverse elements from index 2 to 5 (inclusive)
reversed_middle = numbers[5:1:-1]  # Goes: index 5,4,3,2
result = numbers[:2] + reversed_middle + numbers[6:]

print("Portion (index 2 to 5) reversed:", result)
print("Reversed middle slice:", reversed_middle)
