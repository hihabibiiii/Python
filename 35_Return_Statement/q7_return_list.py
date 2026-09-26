# Question 7 (Medium):
# Define a function called get_factors that takes a positive integer n
# and returns a LIST of all its factors (numbers that divide n evenly).

# Solution:
def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Test with several numbers
for num in [1, 12, 28, 36, 100]:
    factors = get_factors(num)
    print(f"Factors of {num}: {factors}")

# Get number from user
n = int(input("\nEnter a positive integer: "))
if n < 1:
    print("Please enter a positive integer.")
else:
    result = get_factors(n)
    print(f"Factors of {n}: {result}")
    print(f"Number of factors: {len(result)}")

# Example Input:  12
# Example Output: Factors of 12: [1, 2, 3, 4, 6, 12]
