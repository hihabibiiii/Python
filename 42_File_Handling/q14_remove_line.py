# Question: Remove a specific line from a file.
# Read the file, filter out the target line, then rewrite the file.
# Print before and after to show the change.

# Example output:
# Original file:
# 1. Apples
# 2. Bananas
# 3. Cherries  <-- will be removed
# 4. Dates
# 5. Elderberries
#
# Enter the line to remove: 3. Cherries
# Line removed successfully!
#
# Updated file:
# 1. Apples
# 2. Bananas
# 4. Dates
# 5. Elderberries

# Step 1: Create a sample file
original_lines = [
    "1. Apples\n",
    "2. Bananas\n",
    "3. Cherries\n",
    "4. Dates\n",
    "5. Elderberries\n"
]

with open('remove_line.txt', 'w') as f:
    f.writelines(original_lines)

# Step 2: Show original content
print("Original file:")
with open('remove_line.txt', 'r') as f:
    content = f.read()
print(content)

# Step 3: Ask which line to remove
line_to_remove = input("Enter the line to remove: ").strip()

# Step 4: Read, filter, and rewrite
with open('remove_line.txt', 'r') as f:
    lines = f.readlines()

filtered_lines = [line for line in lines if line.strip() != line_to_remove]

if len(filtered_lines) < len(lines):
    with open('remove_line.txt', 'w') as f:
        f.writelines(filtered_lines)
    print("Line removed successfully!")
else:
    print(f"Line '{line_to_remove}' not found in file.")

# Step 5: Show updated content
print("\nUpdated file:")
with open('remove_line.txt', 'r') as f:
    print(f.read(), end='')
