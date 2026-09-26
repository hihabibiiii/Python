# Question:
# Write a recursive function to compute the Nth Fibonacci number.
# fib(0)=0, fib(1)=1, fib(n) = fib(n-1) + fib(n-2)

# Example:
# Enter N: 8
# Fibonacci(8) = 21

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter N (position in Fibonacci sequence): "))
print(f"Fibonacci({n}) = {fib(n)}")
