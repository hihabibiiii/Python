# Question: Append a new line to an existing text file without overwriting it.
# First create a file with initial content, then append a new line to it,
# and finally print the full file to show the appended content.

# Example output:
# Original file created.
# Line appended successfully!
# Final file contents:
# Line 1: Original content.
# Line 2: This line was appended!

# Step 1: Create a file with original content
with open('append_demo.txt', 'w') as f:
    f.write("Line 1: Original content.\n")

print("Original file created.")

# Step 2: Append a new line using 'a' (append) mode
with open('append_demo.txt', 'a') as f:
    f.write("Line 2: This line was appended!\n")

print("Line appended successfully!")

# Step 3: Read and display the full file
with open('append_demo.txt', 'r') as f:
    content = f.read()

print("Final file contents:")
print(content)
