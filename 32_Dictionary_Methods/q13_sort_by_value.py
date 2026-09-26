# Question 13 (Hard):
# Given a dictionary of items and their prices,
# sort the dictionary by value (price) using items() and sorted().
# Print sorted results in both ascending and descending order.

# Solution:
prices = {
    "mango": 3.50,
    "apple": 1.20,
    "blueberry": 5.00,
    "banana": 0.75,
    "cherry": 4.25,
    "grape": 2.10
}

print("Original dictionary:")
for item, price in prices.items():
    print(f"  {item:<12}: ${price:.2f}")

# Sort by value ascending
sorted_asc = sorted(prices.items(), key=lambda item: item[1])
print("\nSorted by price (ascending):")
for item, price in sorted_asc:
    print(f"  {item:<12}: ${price:.2f}")

# Sort by value descending
sorted_desc = sorted(prices.items(), key=lambda item: item[1], reverse=True)
print("\nSorted by price (descending):")
for item, price in sorted_desc:
    print(f"  {item:<12}: ${price:.2f}")

# Convert sorted list of tuples back to dictionary
sorted_dict = dict(sorted_asc)
print("\nAs a sorted dictionary:", sorted_dict)

# Example Output:
# Sorted by price (ascending):
#   banana      : $0.75
#   apple       : $1.20
#   grape       : $2.10
#   mango       : $3.50
#   cherry      : $4.25
#   blueberry   : $5.00
