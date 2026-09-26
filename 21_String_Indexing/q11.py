# Question: Print the character at a user-specified index. Handle IndexError gracefully.
# If the user provides an out-of-range index, display a helpful message instead of crashing.
# Example:
#   String: "Hello"
#   Index: 10 -> Output: Error: Index 10 is out of range for a string of length 5.

text = input("Enter a string: ")
index_str = input("Enter an index: ")

try:
    index = int(index_str)
    print(f"Character at index {index}: '{text[index]}'")
except IndexError:
    print(f"Error: Index {index} is out of range for a string of length {len(text)}.")
except ValueError:
    print("Error: Please enter a valid integer index.")
