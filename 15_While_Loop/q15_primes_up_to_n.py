# Question:
# Take a number N from the user.
# Find all prime numbers from 2 up to N using a while loop (trial division).
# Do NOT use the Sieve of Eratosthenes.
#
# Example:
#   Input: 30
#   Output: Primes up to 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

N = int(input("Enter a number N to find all primes up to N: "))

print(f"\nPrime numbers up to {N}:")
primes = []

num = 2
while num <= N:
    # Check if num is prime using trial division
    is_prime = True
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor = divisor + 1

    if is_prime:
        primes.append(num)
    num = num + 1

if primes:
    print(", ".join(str(p) for p in primes))
else:
    print("No prime numbers found.")
