# Question:
# Simulate a score-keeping system for a game.
# Starting score = 0.
# For each of 5 rounds, ask the user: win or lose?
#   - win: score += 10
#   - lose: score -= 5
# Print the score after each round and the final score.

score = 0
print("Game Score Tracker")
print("------------------")

for i in range(1, 6):
    result = input(f"Round {i} - Did you win or lose? (win/lose): ").strip().lower()
    if result == "win":
        score += 10
        print(f"  +10 points! Score: {score}")
    elif result == "lose":
        score -= 5
        print(f"  -5 points! Score: {score}")
    else:
        print("  Invalid input. No change.")

print(f"\nFinal Score: {score}")
