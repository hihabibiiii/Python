# Question: Use the 'with' statement to open and read a file.
# The 'with' statement automatically closes the file when done — even if an error occurs.
# Create a sample file, then use 'with open(...)' to read it.

# Example output:
# Reading file using 'with' statement (recommended):
# -----------------------------------------
# The with statement is the Pythonic way
# to handle files. It automatically closes
# the file when the block ends, even if
# an error occurs inside the block.
# -----------------------------------------
# File closed automatically after 'with' block!

# Step 1: Create sample file
with open('with_demo.txt', 'w') as f:
    f.write("The with statement is the Pythonic way\n")
    f.write("to handle files. It automatically closes\n")
    f.write("the file when the block ends, even if\n")
    f.write("an error occurs inside the block.\n")

# Step 2: Read using 'with' — the recommended approach
print("Reading file using 'with' statement (recommended):")
print("-" * 41)

with open('with_demo.txt', 'r') as f:
    content = f.read()
    print(content, end='')

print("-" * 41)
# File is automatically closed here — no need to call f.close()
print("File closed automatically after 'with' block!")
