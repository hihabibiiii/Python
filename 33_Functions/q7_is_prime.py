# Question 7 (Medium):
# Define a function called is_prime that takes an integer n
# and returns True if it is prime, False otherwise.
# A prime number is greater than 1 and divisible only by 1 and itself.

# Solution:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test with several numbers
test_numbers = [1, 2, 3, 4, 17, 20, 29, 100]
for num in test_numbers:
    result = is_prime(num)
    print(f"is_prime({num}) = {result}")

# Print primes from 1 to 50
primes = [n for n in range(1, 51) if is_prime(n)]
print(f"\nPrime numbers from 1 to 50: {primes}")

# Get a number from user
n = int(input("\nEnter a number to check: "))
print(f"{n} is {'prime' if is_prime(n) else 'NOT prime'}")

# Example Input:  17
# Example Output: 17 is prime
