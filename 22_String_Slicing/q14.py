# Question: Take a string and interleave two slices: even-indexed characters followed by
#           odd-indexed characters. (Separate the two groups, then concatenate.)
# Example:
#   Input: "Python"
#   Even-indexed (0,2,4): "Pto"
#   Odd-indexed  (1,3,5): "yhn"
#   Interleaved result:   "Ptoyhn"

text = input("Enter a string: ")
even_part = text[::2]   # characters at indices 0, 2, 4, ...
odd_part  = text[1::2]  # characters at indices 1, 3, 5, ...
result = even_part + odd_part
print("Even-indexed characters:", even_part)
print("Odd-indexed characters:", odd_part)
print("Interleaved (even + odd):", result)
