# Question: Write the numbers 1 to 100 to a file (one per line).
# Then read the file and compute the sum of all numbers.
# Print the sum and verify it equals 5050.

# Example output:
# Numbers 1-100 written to 'numbers.txt'.
# Reading numbers and computing sum...
# Sum of numbers 1 to 100: 5050
# Verification: 1+2+...+100 = n*(n+1)/2 = 5050 ✓

# Step 1: Write numbers 1-100 to file
with open('numbers.txt', 'w') as f:
    for i in range(1, 101):
        f.write(str(i) + '\n')

print("Numbers 1-100 written to 'numbers.txt'.")

# Step 2: Read file and compute sum
total = 0
count = 0

print("Reading numbers and computing sum...")
with open('numbers.txt', 'r') as f:
    for line in f:
        number = int(line.strip())
        total += number
        count += 1

print(f"Numbers read: {count}")
print(f"Sum of numbers 1 to 100: {total}")

# Verification using formula n*(n+1)/2
expected = 100 * 101 // 2
print(f"Verification: 1+2+...+100 = n*(n+1)/2 = {expected}", "✓" if total == expected else "✗")
