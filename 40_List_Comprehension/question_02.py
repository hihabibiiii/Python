# Question:
# Create a list of even numbers from 1 to 30 using list comprehension.

evens = [x for x in range(1, 31) if x % 2 == 0]
print(f"Even numbers 1-30: {evens}")
