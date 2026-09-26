# Question: Count the number of lines in a text file.
# Create a sample file with multiple lines, then count and print the total.

# Example output:
# File 'count_lines.txt' created with sample content.
# Total lines in the file: 7

# Step 1: Create a sample file
sample_text = """Alice went to the store.
She bought apples and bananas.
Then she walked home.
It was a sunny day.
The birds were singing.
She made a fruit salad.
It was delicious!"""

with open('count_lines.txt', 'w') as f:
    f.write(sample_text)

print("File 'count_lines.txt' created with sample content.")

# Step 2: Count lines
with open('count_lines.txt', 'r') as f:
    lines = f.readlines()   # Returns list of all lines

line_count = len(lines)
print(f"Total lines in the file: {line_count}")
