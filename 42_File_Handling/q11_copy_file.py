# Question: Copy the content of one file to another file.
# Read from 'source.txt' and write everything into 'destination.txt'.
# Print confirmation and the content of the destination file.

# Example output:
# Source file created.
# Copying 'source.txt' to 'destination.txt'...
# Copy complete! 42 characters copied.
# 
# Contents of destination.txt:
# Hello from the source file!
# This is line 2.
# And this is line 3.

# Step 1: Create source file
with open('source.txt', 'w') as f:
    f.write("Hello from the source file!\n")
    f.write("This is line 2.\n")
    f.write("And this is line 3.\n")

print("Source file created.")

# Step 2: Copy source to destination
print("Copying 'source.txt' to 'destination.txt'...")

with open('source.txt', 'r') as src:
    content = src.read()

with open('destination.txt', 'w') as dst:
    dst.write(content)

print(f"Copy complete! {len(content)} characters copied.")

# Step 3: Verify by reading destination
print("\nContents of destination.txt:")
with open('destination.txt', 'r') as f:
    print(f.read(), end='')
