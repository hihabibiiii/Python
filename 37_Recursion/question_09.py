# Question:
# Write a recursive binary search function.
# Search for a target in a SORTED list.
# Return the index if found, -1 if not found.

# Example:
# List: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Enter target: 11
# Found at index: 5

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"List: {data}")
target = int(input("Enter target to search: "))

result = binary_search(data, target, 0, len(data) - 1)
if result != -1:
    print(f"Found at index: {result}")
else:
    print(f"{target} not found in the list.")
