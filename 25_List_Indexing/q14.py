# Question: Given a list, find all indices where the value exceeds a user-defined threshold.
# Example:
#   List: [15, 42, 8, 73, 29, 55, 6, 91]
#   Threshold: 40
#   Indices where value > 40: [1, 3, 5, 7]  (values: 42, 73, 55, 91)

numbers = [15, 42, 8, 73, 29, 55, 6, 91]
print("List:", numbers)

threshold = int(input("Enter the threshold value: "))

exceeding_indices = []
for i in range(len(numbers)):
    if numbers[i] > threshold:
        exceeding_indices.append(i)

print(f"\nIndices where value > {threshold}:")
for idx in exceeding_indices:
    print(f"  Index {idx}: value = {numbers[idx]}")
print("Indices list:", exceeding_indices)
