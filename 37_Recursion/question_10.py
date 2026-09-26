# Question:
# Write a recursive function to count occurrences of a character in a string.
# count_char("banana", "a") = 3

# Example:
# Enter a string: mississippi
# Enter a character: s
# 's' appears 4 times.

def count_char(s, ch):
    if len(s) == 0:
        return 0
    count = 1 if s[0] == ch else 0
    return count + count_char(s[1:], ch)

text = input("Enter a string: ")
char = input("Enter a character: ")
result = count_char(text, char)
print(f"'{char}' appears {result} time(s) in '{text}'.")
