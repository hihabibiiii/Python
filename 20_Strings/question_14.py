# Question:
# Take a string from the user.
# Find and print the most frequent character (excluding spaces).

# Example:
# Enter a string: programming
# Most frequent character: 'g' (appears 2 times)

text = input("Enter a string: ")

# Count frequency of each character (manually)
chars = {}
for ch in text:
    if ch == " ":
        continue
    if ch in chars:
        chars[ch] += 1
    else:
        chars[ch] = 1

# Find the max frequency
max_char = ""
max_count = 0
for ch, count in chars.items():
    if count > max_count:
        max_count = count
        max_char = ch

print(f"Most frequent character: '{max_char}' (appears {max_count} time(s))")
