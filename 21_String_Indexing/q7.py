# Question: Take a 5-letter word and print its characters at positions 1 and 3 (0-indexed).
# Example:
#   Input: "plant"
#   Output: Character at position 1: l
#           Character at position 3: n

word = input("Enter a 5-letter word: ")
if len(word) == 5:
    print("Character at position 1:", word[1])
    print("Character at position 3:", word[3])
else:
    print("Please enter exactly 5 letters.")
