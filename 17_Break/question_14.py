# Question:
# Implement linear search using break.
# Search for a target value in a list.
# Print the index if found, or -1 if not found.

# Example:
# List: [10, 25, 3, 47, 8, 92]
# Enter value to search: 47
# Found at index: 3

data = [10, 25, 3, 47, 8, 92]
print(f"List: {data}")
target = int(input("Enter value to search: "))

result = -1
for i in range(len(data)):
    if data[i] == target:
        result = i
        break

if result != -1:
    print(f"Found at index: {result}")
else:
    print("Value not found. Index: -1")
