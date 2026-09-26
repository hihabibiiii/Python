# Question 7 (Medium):
# Create a dictionary of at least 4 items (e.g. product prices).
# Use a for loop to iterate over keys and values and print each pair
# in the format: "Key: ... | Value: ..."

# Solution:
prices = {
    "apple": 1.20,
    "banana": 0.50,
    "cherry": 2.50,
    "date": 3.75,
    "elderberry": 5.00
}

print("Product Prices:")
print("-" * 30)
for key, value in prices.items():
    print(f"Key: {key:<12} | Value: ${value:.2f}")

# Example Output:
# Product Prices:
# ------------------------------
# Key: apple        | Value: $1.20
# Key: banana       | Value: $0.50
# Key: cherry       | Value: $2.50
# Key: date         | Value: $3.75
# Key: elderberry   | Value: $5.00
