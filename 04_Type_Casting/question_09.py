# Question 9 (Medium):
# Take a string of digits from the user (e.g. '12345').
# Iterate over each character, convert to int, and compute their sum.

# Solution:
digit_string = input("Enter a string of digits (e.g. 12345): ")

total = 0
for char in digit_string:
    total = total + int(char)

print("Digit string:", digit_string)
print("Sum of digits:", total)

# Example Input / Output:
# Enter a string of digits (e.g. 12345): 12345
# Digit string: 12345
# Sum of digits: 15
