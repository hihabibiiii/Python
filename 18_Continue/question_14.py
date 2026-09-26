# Question:
# Ask the user to enter 10 values one by one.
# Try to convert each to an integer.
# If conversion fails, use `continue` to skip invalid input.
# Sum all valid integers and print the total.

total = 0
valid_count = 0

for i in range(1, 11):
    raw = input(f"Enter value {i}: ")
    try:
        num = int(raw)
    except ValueError:
        print(f"  '{raw}' is not a valid integer. Skipping.")
        continue
    total += num
    valid_count += 1

print(f"\nValid inputs: {valid_count}")
print(f"Sum of valid integers: {total}")
