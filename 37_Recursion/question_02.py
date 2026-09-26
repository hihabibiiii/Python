# Question:
# Write a recursive function to compute the sum of 1 + 2 + 3 + ... + N.

# Example:
# Enter N: 5
# Sum from 1 to 5 = 15

def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

n = int(input("Enter N: "))
result = recursive_sum(n)
print(f"Sum from 1 to {n} = {result}")
