# Question: Read the content of a text file and print it to the console.
# First, create a sample file 'data.txt' with some text, then read and print it.

# Example output:
# Contents of data.txt:
# -----------------------
# Python is amazing!
# File handling is easy.
# Let's keep learning.
# -----------------------

# Step 1: Create a sample file to read
with open('data.txt', 'w') as f:
    f.write("Python is amazing!\nFile handling is easy.\nLet's keep learning.")

# Step 2: Read and print the content
file = open('data.txt', 'r')
content = file.read()
file.close()

print("Contents of data.txt:")
print("-" * 23)
print(content)
print("-" * 23)
