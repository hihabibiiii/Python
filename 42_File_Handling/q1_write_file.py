# Question: Write the string 'Hello, File!' to a text file called 'output.txt'.
# Then close the file and print a confirmation message.
# Open and verify by printing the content.

# Example output:
# 'Hello, File!' has been written to output.txt
# Verification - File contents: Hello, File!

# Write to file
file = open('output.txt', 'w')
file.write('Hello, File!')
file.close()
print("'Hello, File!' has been written to output.txt")

# Verify by reading back
file = open('output.txt', 'r')
content = file.read()
file.close()
print(f"Verification - File contents: {content}")
