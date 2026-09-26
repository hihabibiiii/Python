# Question:
# Check which numbers from 2 to 50 are prime using nested loops.
# The outer loop goes through each number.
# The inner loop checks for divisors.
#
# Expected Output:
#   Prime numbers from 2 to 50:
#   2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47

print("Prime numbers from 2 to 50:")
primes = []

for num in range(2, 51):
    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print(", ".join(str(p) for p in primes))
