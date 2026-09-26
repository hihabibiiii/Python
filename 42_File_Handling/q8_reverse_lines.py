# Question: Read a file and print its lines in REVERSE order.
# Create a sample file, read all lines, then print from last to first.

# Example output:
# Original file lines:
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# 
# Lines in REVERSE order:
# Line 5
# Line 4
# Line 3
# Line 2
# Line 1

# Step 1: Create sample file
with open('reverse_lines.txt', 'w') as f:
    for i in range(1, 6):
        f.write(f"Line {i}\n")

# Step 2: Read all lines
with open('reverse_lines.txt', 'r') as f:
    lines = f.readlines()

# Show original order
print("Original file lines:")
for line in lines:
    print(line.strip())

# Step 3: Print in reverse
print("\nLines in REVERSE order:")
for line in reversed(lines):
    print(line.strip())
