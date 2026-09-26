# Question: Import the random module and generate a random integer between 1 and 100.
# Run the program a few times to see different results each time.

# Example output:
# Generating 5 random numbers between 1 and 100:
# Random number 1: 47
# Random number 2: 83
# Random number 3: 12
# Random number 4: 61
# Random number 5: 29

import random

print("Generating 5 random numbers between 1 and 100:")
for i in range(1, 6):
    num = random.randint(1, 100)
    print(f"Random number {i}: {num}")

print()
# Generate a single random number on demand
user_choice = input("Press Enter to generate your lucky number! ")
lucky_number = random.randint(1, 100)
print(f"Your lucky number is: {lucky_number}")
