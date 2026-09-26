# Question:
# Find the first prime number greater than 50.
# Use break when found.

# Example Output:
# First prime greater than 50: 53

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(51, 1000):
    if is_prime(num):
        print(f"First prime greater than 50: {num}")
        break
