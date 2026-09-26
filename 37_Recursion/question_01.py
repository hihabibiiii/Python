# Question:
# Write a recursive function to print countdown from N to 1.

# Example:
# Enter N: 5
# 5 4 3 2 1
# Blast off!

def countdown(n):
    if n <= 0:
        return
    print(n, end=" ")
    countdown(n - 1)

n = int(input("Enter N: "))
countdown(n)
print("\nBlast off!")
