# Question: Use strip() to remove leading and trailing whitespace from a string.
# strip() removes spaces (and other whitespace) from both ends.
# Example:
#   Input (hardcoded): '   hello world   '
#   Output: 'hello world'

text = '   hello world   '
print("Original (with spaces): '" + text + "'")
cleaned = text.strip()
print("After strip(): '" + cleaned + "'")
