# Question:
# Ask the user to enter words one by one.
# Stop when the user types "stop".
# Print all collected words at the end.

# Example:
# Enter a word (or "stop" to end): apple
# Enter a word (or "stop" to end): banana
# Enter a word (or "stop" to end): stop
# Words collected: ['apple', 'banana']

words = []
while True:
    word = input('Enter a word (or "stop" to end): ').strip()
    if word.lower() == "stop":
        break
    words.append(word)

print(f"Words collected: {words}")
