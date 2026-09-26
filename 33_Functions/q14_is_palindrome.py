# Question 14 (Hard):
# Define a function called is_palindrome that takes a string and returns
# True if it is a palindrome (reads the same forwards and backwards),
# False otherwise. Ignore spaces and capitalization.

# Solution:
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# Test cases
test_cases = [
    "racecar",
    "hello",
    "A man a plan a canal Panama",
    "Was it a car or a cat I saw",
    "Python",
    "Madam"
]

print(f"{'String':<35} {'Palindrome?'}")
print("-" * 50)
for s in test_cases:
    result = is_palindrome(s)
    print(f"'{s}'  -->  {result}")

# Get input from user
user_input = input("\nEnter a word or phrase: ")
if is_palindrome(user_input):
    print(f"'{user_input}' IS a palindrome!")
else:
    print(f"'{user_input}' is NOT a palindrome.")

# Example Input:  racecar
# Example Output: 'racecar' IS a palindrome!
