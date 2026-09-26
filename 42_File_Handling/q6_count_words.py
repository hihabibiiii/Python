# Question: Count the total number of words in a text file.
# Create a sample file, then read it and count all the words.

# Example output:
# File created.
# Total words in the file: 30

# Step 1: Create a sample file
sample_text = """Python is a powerful programming language.
It is widely used in data science and machine learning.
File handling allows us to read and write data.
Word counting is a common text processing task.
Practice coding every day to improve your skills."""

with open('word_count.txt', 'w') as f:
    f.write(sample_text)

print("File created.")

# Step 2: Count words
total_words = 0

with open('word_count.txt', 'r') as f:
    for line in f:
        words = line.split()  # Split line into words
        total_words += len(words)

print(f"Total words in the file: {total_words}")
