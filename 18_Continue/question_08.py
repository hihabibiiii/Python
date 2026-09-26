# Question:
# Loop through a string character by character.
# Skip spaces using `continue`.
# Count and print the number of non-space characters.

# Example:
# Enter a string: Hello World
# Non-space characters: 10

text = input("Enter a string: ")
count = 0

for ch in text:
    if ch == " ":
        continue
    count += 1

print(f"Non-space characters: {count}")
