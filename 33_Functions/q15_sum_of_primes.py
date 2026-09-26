# Question 15 (Hard):
# Define two functions:
#   1. is_prime(n)  - returns True if n is prime
#   2. sum_of_primes(n) - returns the sum of all prime numbers up to n (inclusive)
# Use is_prime inside sum_of_primes (function composition).

# Solution:
def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(n):
    """Return the sum of all prime numbers from 2 up to n (inclusive)."""
    total = 0
    for num in range(2, n + 1):
        if is_prime(num):
            total += num
    return total

# Display primes and running sum
limit = int(input("Enter the upper limit N: "))

prime_list = [num for num in range(2, limit + 1) if is_prime(num)]
print(f"\nPrime numbers up to {limit}:")
print(prime_list)
print(f"\nNumber of primes: {len(prime_list)}")
print(f"Sum of all primes up to {limit}: {sum_of_primes(limit)}")

# Example Input:  20
# Example Output:
# Prime numbers up to 20: [2, 3, 5, 7, 11, 13, 17, 19]
# Number of primes: 8
# Sum of all primes up to 20: 77
