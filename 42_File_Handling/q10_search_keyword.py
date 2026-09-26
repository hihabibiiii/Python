# Question: Search for a keyword in a file and print all lines that contain it.
# Ask the user to enter a keyword, then print matching lines with line numbers.

# Example output:
# Keyword to search: python
# 
# Searching in 'search_demo.txt' for 'python'...
# Found 2 matching line(s):
#   Line 1: Python is a popular programming language.
#   Line 3: Many data scientists use python daily.

# Step 1: Create sample file
sample_text = """Python is a popular programming language.
Java and C++ are also widely used.
Many data scientists use python daily.
Web developers often choose JavaScript.
Python can be used for automation too."""

with open('search_demo.txt', 'w') as f:
    f.write(sample_text)

# Step 2: Search for keyword
keyword = input("Keyword to search: ").strip()
print(f"\nSearching in 'search_demo.txt' for '{keyword}'...")

matches = []

with open('search_demo.txt', 'r') as f:
    for line_num, line in enumerate(f, start=1):
        if keyword.lower() in line.lower():  # Case-insensitive search
            matches.append((line_num, line.strip()))

if matches:
    print(f"Found {len(matches)} matching line(s):")
    for line_num, line in matches:
        print(f"  Line {line_num}: {line}")
else:
    print(f"No lines containing '{keyword}' were found.")
