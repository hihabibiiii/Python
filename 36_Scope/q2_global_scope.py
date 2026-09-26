# Question 2 (Easy):
# Demonstrate GLOBAL scope: define a variable at module level
# and read it from inside a function (read-only access).

# Solution:
global_message = "I am a global variable"
pi = 3.14159

def show_globals():
    # We can READ global variables without any keyword
    print("Inside function, accessing global_message:", global_message)
    print("Inside function, accessing pi:", pi)

show_globals()

# Globals are also accessible outside the function
print("Outside function, global_message:", global_message)

# Example Output:
# Inside function, accessing global_message: I am a global variable
# Inside function, accessing pi: 3.14159
# Outside function, global_message: I am a global variable
