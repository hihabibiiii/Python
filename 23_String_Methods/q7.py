# Question: Use count() to count the occurrences of a substring in a string.
# Example:
#   String: "banana"
#   Substring: "an"
#   Output: 'an' appears 2 time(s) in 'banana'.

text = input("Enter a string: ")
sub = input("Enter the substring to count: ")

occurrences = text.count(sub)
print(f"'{sub}' appears {occurrences} time(s) in '{text}'.")
