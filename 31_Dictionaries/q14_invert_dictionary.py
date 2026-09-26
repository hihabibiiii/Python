# Question 14 (Hard):
# Given a dictionary, invert it so that the original values become keys
# and the original keys become values.
# Print both the original and the inverted dictionary.
# Note: This works correctly when all values are unique and hashable.

# Solution:
original = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}

print("Original dictionary:", original)

inverted = {}
for key, value in original.items():
    inverted[value] = key

print("Inverted dictionary:", inverted)

# Another example: country -> capital (inverted: capital -> country)
country_capital = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasilia",
    "Egypt": "Cairo"
}

capital_country = {}
for country, capital in country_capital.items():
    capital_country[capital] = country

print("\nCountry -> Capital:", country_capital)
print("Capital -> Country:", capital_country)

# Example Output:
# Original dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Inverted dictionary: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
