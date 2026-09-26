# Question:
# Take a number from the user and check if it is a prime number using a for loop.
# A prime number is greater than 1 and has no divisors other than 1 and itself.
#
# Example:
#   Input: 7   -> Output: 7 is a prime number.
#   Input: 12  -> Output: 12 is NOT a prime number.

number = int(input("Enter a number to check if it's prime: "))

if number < 2:
    print(f"{number} is NOT a prime number (must be greater than 1).")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break  # No need to check further

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is NOT a prime number.")
