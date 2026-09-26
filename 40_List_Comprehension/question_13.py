# Question:
# Create a list of prime numbers from 2 to 50 using list comprehension.
# Use a helper function is_prime() inside the comprehension.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(2, 51) if is_prime(n)]
print(f"Prime numbers from 2 to 50:")
print(primes)
print(f"Count: {len(primes)}")
