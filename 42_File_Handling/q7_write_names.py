# Question: Write a list of names to a file, one name per line.
# Then read the file and print each name with a greeting.

# Example output:
# Names written to 'names.txt' successfully!
# 
# Reading names from file:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
# Hello, Diana!
# Hello, Ethan!

names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

# Write names to file (one per line)
with open('names.txt', 'w') as f:
    for name in names:
        f.write(name + '\n')

print("Names written to 'names.txt' successfully!")
print()

# Read and greet each name
print("Reading names from file:")
with open('names.txt', 'r') as f:
    for line in f:
        name = line.strip()  # Remove newline character
        if name:             # Skip empty lines
            print(f"Hello, {name}!")
