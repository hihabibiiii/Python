# Question: Rotate a string right by k positions using slicing.
# A right rotation by k moves the last k characters to the front.
# Example:
#   Input: "Python", k=2
#   Output: onPyth
#   Explanation: Last 2 chars "on" move to front -> "on" + "Pyth" = "onPyth"

text = input("Enter a string: ")
k = int(input("Enter the number of positions to rotate right (k): "))

# Handle k larger than string length
k = k % len(text) if len(text) > 0 else 0

rotated = text[-k:] + text[:-k]
print("Original string:", text)
print(f"After right rotation by {k}:", rotated)
