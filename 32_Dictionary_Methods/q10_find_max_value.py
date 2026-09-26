# Question 10 (Medium):
# Given a dictionary of player names and their scores,
# iterate over items() to find the player with the maximum score.
# Print the winner.

# Solution:
scores = {
    "Alice": 87,
    "Bob": 95,
    "Carol": 72,
    "David": 91,
    "Eve": 88
}

print("Player Scores:")
for player, score in scores.items():
    print(f"  {player}: {score}")

# Find max using items() iteration
max_player = None
max_score = -1

for player, score in scores.items():
    if score > max_score:
        max_score = score
        max_player = player

print(f"\nWinner: {max_player} with a score of {max_score}")

# Also demonstrate using max() with key
winner = max(scores.items(), key=lambda item: item[1])
print(f"Confirmed with max(): {winner[0]} scored {winner[1]}")

# Example Output:
# Winner: Bob with a score of 95
