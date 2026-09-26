# Question:
# Implement a number guessing game.
# The secret number is 42.
# Keep asking the user to guess until they get it right.
# Count the number of attempts.
# Give hints: 'Too low!' or 'Too high!' after each wrong guess.
#
# Example:
#   Guess: 20 -> Too low!
#   Guess: 60 -> Too high!
#   Guess: 42 -> Correct! You guessed it in 3 attempts.

SECRET = 42
attempts = 0

print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100...")

guess = int(input("Your guess: "))
attempts = 1

while guess != SECRET:
    if guess < SECRET:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Your guess: "))
    attempts = attempts + 1

print(f"Correct! You guessed it in {attempts} attempt(s)!")
