# Question:
# Compute the average of numbers in a list.
# Skip negative numbers and zeros using `continue`.
# List: [4, -2, 7, 0, 3, -1, 8]

# Example Output:
# Valid numbers: [4, 7, 3, 8]
# Average: 5.5

data = [4, -2, 7, 0, 3, -1, 8]
total = 0
count = 0
valid = []

for num in data:
    if num <= 0:
        continue
    total += num
    count += 1
    valid.append(num)

print(f"Valid numbers: {valid}")
if count > 0:
    print(f"Average: {total / count:.2f}")
else:
    print("No valid numbers found.")
