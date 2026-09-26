# Question:
# ATM PIN verification with 3 attempts.
# Correct PIN is "5678".
# Allow 3 attempts; use break when correct PIN is entered.

# Example:
# Attempt 1: Enter PIN: 1234
# Wrong PIN. Try again.
# Attempt 2: Enter PIN: 5678
# PIN accepted. Access granted!

correct_pin = "5678"

for attempt in range(1, 4):
    entered = input(f"Attempt {attempt}: Enter PIN: ").strip()
    if entered == correct_pin:
        print("PIN accepted. Access granted!")
        break
    else:
        remaining = 3 - attempt
        if remaining > 0:
            print(f"Wrong PIN. {remaining} attempt(s) remaining.")
        else:
            print("Card blocked after 3 failed attempts.")
