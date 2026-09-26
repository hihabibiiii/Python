# Question: Read a text file line by line using a for loop.
# Create a sample file with 5 lines, then read and print each line
# with its line number.

# Example output:
# Reading file line by line:
# Line 1: The quick brown fox
# Line 2: jumps over the lazy dog
# Line 3: Python is a great language
# Line 4: File handling is useful
# Line 5: Practice makes perfect

# Step 1: Create a sample file
lines = [
    "The quick brown fox\n",
    "jumps over the lazy dog\n",
    "Python is a great language\n",
    "File handling is useful\n",
    "Practice makes perfect\n"
]

with open('lines_demo.txt', 'w') as f:
    f.writelines(lines)

# Step 2: Read line by line using a for loop
print("Reading file line by line:")
with open('lines_demo.txt', 'r') as f:
    for line_number, line in enumerate(f, start=1):
        print(f"Line {line_number}: {line.strip()}")
