# Question: Take a list of numbers and separate them into two lists: evens and odds.
# Use a loop and the modulo operator (%) to classify each number.
# Example:
#   Input:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   Evens: [2, 4, 6, 8, 10]
#   Odds:  [1, 3, 5, 7, 9]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Numbers:", numbers)

evens = []
odds = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print("Even numbers:", evens)
print("Odd numbers:", odds)
