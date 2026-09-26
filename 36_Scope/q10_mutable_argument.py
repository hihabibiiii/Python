# Question 10 (Medium):
# Demonstrate that MUTABLE objects (like lists) passed to a function
# CAN be modified via methods — the outer variable reflects the change.

# Solution:
def add_item(my_list, item):
    my_list.append(item)   # modifies the SAME list in memory
    print(f"  Inside function, my_list = {my_list}")

shopping = ["milk", "bread"]
print("Before function call:", shopping)
add_item(shopping, "eggs")
add_item(shopping, "butter")
print("After function calls:", shopping)

# Contrast: reassigning the list variable does NOT affect outer
def replace_list(my_list):
    my_list = ["completely", "new", "list"]   # creates new local binding
    print(f"  Inside replace_list: {my_list}")

print("\nTrying to replace the list:")
print("Before:", shopping)
replace_list(shopping)
print("After: ", shopping)  # unchanged

# Example Output:
# Before function call: ['milk', 'bread']
# After function calls: ['milk', 'bread', 'eggs', 'butter']
#
# Trying to replace the list:
# Before: ['milk', 'bread', 'eggs', 'butter']
# After:  ['milk', 'bread', 'eggs', 'butter']   (unchanged)
