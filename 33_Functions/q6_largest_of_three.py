# Question 6 (Medium):
# Define a function called largest_of_three that takes three numbers
# as parameters and returns the largest one.

# Solution:
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Test cases
print("Largest of 10, 25, 7:", largest_of_three(10, 25, 7))
print("Largest of 100, 100, 50:", largest_of_three(100, 100, 50))
print("Largest of -5, -3, -10:", largest_of_three(-5, -3, -10))

# Get three numbers from user
a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print(f"Largest of {a}, {b}, {c}: {largest_of_three(a, b, c)}")

# Example Input:  3, 8, 5
# Example Output: Largest of 3.0, 8.0, 5.0: 8.0
