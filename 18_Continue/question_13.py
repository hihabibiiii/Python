# Question:
# Process a CSV-style string: "10,abc,20,xyz,30"
# Split by comma, skip non-numeric values using `continue`.
# Sum only the numeric values.

# Example Output:
# Skipping: abc
# Skipping: xyz
# Sum of numeric values: 60

csv_string = "10,abc,20,xyz,30"
parts = csv_string.split(",")
total = 0

for part in parts:
    try:
        num = int(part)
    except ValueError:
        print(f"Skipping: {part}")
        continue
    total += num

print(f"Sum of numeric values: {total}")
