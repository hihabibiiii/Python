# Question: Use random.shuffle() to shuffle a list in place.
# Create a deck of cards (simplified), shuffle it, and deal the top 5 cards.

# Example output:
# Original deck (first 10 cards): ['A♠', 'K♠', 'Q♠', 'J♠', '10♠', ...]
# 
# Shuffling deck...
# Shuffled deck (first 10 cards): ['7♥', 'Q♦', '3♠', 'K♣', ...]
# 
# Dealing 5 cards:
# Card 1: 7♥
# Card 2: Q♦
# Card 3: 3♠
# Card 4: K♣
# Card 5: 9♦

import random

# Create a simplified deck
suits = ['♠', '♥', '♦', '♣']
ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

deck = [rank + suit for suit in suits for rank in ranks]

print(f"Original deck (first 10 cards): {deck[:10]}")
print(f"Total cards in deck: {len(deck)}")

# Shuffle the deck in place
print("\nShuffling deck...")
random.shuffle(deck)

print(f"Shuffled deck (first 10 cards): {deck[:10]}")

# Deal 5 cards
print("\nDealing 5 cards:")
for i in range(1, 6):
    card = deck.pop(0)  # Deal from top of deck
    print(f"  Card {i}: {card}")

print(f"\nCards remaining in deck: {len(deck)}")
