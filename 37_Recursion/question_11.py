# Question:
# Write a recursive function to compute GCD of two numbers.
# Using Euclidean algorithm: gcd(a, b) = gcd(b, a%b), base: gcd(a, 0) = a

# Example:
# Enter a: 48
# Enter b: 18
# GCD(48, 18) = 6

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"GCD({a}, {b}) = {gcd(a, b)}")
