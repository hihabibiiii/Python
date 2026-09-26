# Question 4 (Easy):
# Show that a LOCAL variable with the same name as a global variable
# SHADOWS the global inside the function. The global is unchanged.

# Solution:
x = "global x"
print("Before function call, x =", x)

def shadow():
    x = "local x"   # creates a new local variable, does NOT change global x
    print("Inside shadow(), x =", x)

shadow()

print("After function call, x =", x)  # global x unchanged

# Example Output:
# Before function call, x = global x
# Inside shadow(), x = local x
# After function call, x = global x

# --- Another example ---
temperature = 100   # global

def show_temp():
    temperature = 37    # local shadow
    print("  Body temperature inside function:", temperature)

print("\nGlobal temperature:", temperature)
show_temp()
print("Global temperature after function:", temperature)
