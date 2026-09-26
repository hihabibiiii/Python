# Question 9 (Medium):
# Define a function called count_vowels that takes a string as input
# and returns the number of vowels (a, e, i, o, u) in it.

# Solution:
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Test with examples
test_strings = ["Hello World", "Python", "aeiou", "bcdfg", "Beautiful"]
for s in test_strings:
    print(f"count_vowels('{s}') = {count_vowels(s)}")

# Get string from user
user_string = input("\nEnter a string: ")
vowel_count = count_vowels(user_string)
print(f"Number of vowels in '{user_string}': {vowel_count}")

# Example Input:  Programming is fun
# Example Output: Number of vowels in 'Programming is fun': 5
