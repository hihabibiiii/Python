# Question: Given a string, create a new string that has the first 3 and last 3 characters.
# Use positive and negative indexing to extract the desired characters.
# Example:
#   Input: "programming"
#   Output: proing

text = input("Enter a string (at least 6 characters): ")
if len(text) < 6:
    print("String must have at least 6 characters.")
else:
    first_three = text[0] + text[1] + text[2]
    last_three = text[-3] + text[-2] + text[-1]
    result = first_three + last_three
    print("First 3 + Last 3 characters:", result)
