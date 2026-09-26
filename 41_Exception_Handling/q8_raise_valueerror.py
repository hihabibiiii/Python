# Question: Manually raise a ValueError with a custom message.
# Ask the user for their age. If the age is negative or over 150,
# raise a ValueError with a descriptive message.

# Example:
# Enter your age: -5
# Error: Age cannot be negative. You entered: -5

# Enter your age: 200
# Error: Age seems unrealistic. You entered: 200

# Enter your age: 25
# Valid age entered: 25

def validate_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative. You entered: {age}")
    if age > 150:
        raise ValueError(f"Age seems unrealistic. You entered: {age}")
    return age

try:
    age = int(input("Enter your age: "))
    valid_age = validate_age(age)
    print(f"Valid age entered: {valid_age}")
except ValueError as e:
    print(f"Error: {e}")
