# Question:
# Write a recursive function to compute base^exp (power).
# power(base, 0) = 1
# power(base, exp) = base * power(base, exp-1)

# Example:
# Enter base: 2
# Enter exponent: 10
# 2^10 = 1024

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print(f"{base}^{exp} = {power(base, exp)}")
