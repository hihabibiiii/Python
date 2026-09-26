# Question: Given a long string, replace the middle section with '***' using slicing.
# Keep the first 3 and last 3 characters; replace everything in between with ***.
# Example:
#   Input: "Hello, World!"
#   Output: Hel***ld!

text = input("Enter a string (at least 7 characters): ")
if len(text) < 7:
    print("String must have at least 7 characters.")
else:
    result = text[:3] + "***" + text[-3:]
    print("Original:", text)
    print("Modified:", result)
