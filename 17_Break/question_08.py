# Question:
# Loop through a list of numbers.
# Use break when the first negative number is encountered.
# Print the negative number and how many positives came before it.

# Example:
# Numbers: [4, 7, 2, 9, -3, 5, -1]
# Found negative: -3 after 4 positive numbers.

numbers = [4, 7, 2, 9, -3, 5, -1]
count = 0

for num in numbers:
    if num < 0:
        print(f"Found negative: {num} after {count} positive number(s).")
        break
    count += 1
else:
    print("No negative numbers found.")
