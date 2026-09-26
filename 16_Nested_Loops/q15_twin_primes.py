# Question:
# Find all twin prime pairs up to 100 using nested loops.
# Twin primes are pairs of prime numbers that differ by 2.
# Examples: (3, 5), (5, 7), (11, 13), (17, 19), (29, 31)...
#
# Step 1: Outer loop - find all primes up to 100 using inner loop.
# Step 2: Check if (prime + 2) is also prime.

def is_prime_check(num):
    if num < 2:
        return False
    for d in range(2, num):
        if num % d == 0:
            return False
    return True

print("Twin prime pairs up to 100:")
twin_pairs = []

for num in range(2, 99):  # Check up to 99 so num+2 <= 101
    if is_prime_check(num) and is_prime_check(num + 2):
        twin_pairs.append((num, num + 2))

for pair in twin_pairs:
    print(f"  {pair}")

print(f"\nTotal twin prime pairs found: {len(twin_pairs)}")
