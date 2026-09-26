# Question:
# Write a recursive function to compute the sum of digits of a number.
# digit_sum(123) = 1 + 2 + 3 = 6

# Example:
# Enter a number: 4567
# Sum of digits of 4567 = 22

def digit_sum(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

n = int(input("Enter a number: "))
print(f"Sum of digits of {n} = {digit_sum(n)}")
