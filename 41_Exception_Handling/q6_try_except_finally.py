# Question: Demonstrate the try/except/finally block.
# The 'finally' block ALWAYS runs, whether an exception occurred or not.
# Simulate a database connection: open a connection, do work, always close it.

# Example (no error):
# Connecting to database...
# Fetching data for user ID: 5
# Data fetched successfully!
# Closing database connection... (always runs)

# Example (error):
# Connecting to database...
# Fetching data for user ID: abc
# Error: User ID must be a number!
# Closing database connection... (always runs)

print("Connecting to database...")

try:
    user_id = int(input("Enter user ID: "))
    print(f"Fetching data for user ID: {user_id}")
    # Simulate successful data fetch
    if user_id <= 0:
        raise ValueError("User ID must be a positive number!")
    print("Data fetched successfully!")
except ValueError as e:
    print(f"Error: {e}")
finally:
    # This ALWAYS runs — like closing a file or connection
    print("Closing database connection... (always runs)")
