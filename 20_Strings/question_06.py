# Question:
# Take a string and a character from the user.
# Count how many times the character appears in the string.
# Do this manually using a loop (not the count() method).

# Example:
# Enter a string: banana
# Enter a character: a
# 'a' appears 3 times.

text = input("Enter a string: ")
char = input("Enter a character: ")

count = 0
for ch in text:
    if ch == char:
        count += 1

print(f"'{char}' appears {count} time(s).")
