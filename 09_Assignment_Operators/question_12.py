# Question:
# Simulate a countdown timer.
# Start at 100 and use -= 10 inside a while loop.
# Print the value every 10 steps until it reaches 0.

# Example Output:
# Countdown: 90
# Countdown: 80
# ...
# Countdown: 0
# Countdown complete!

timer = 100
while timer > 0:
    timer -= 10
    print(f"Countdown: {timer}")

print("Countdown complete!")
