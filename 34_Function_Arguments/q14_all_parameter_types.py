# Question 14 (Hard):
# Write a function with ALL parameter types:
#   positional, default, *args, keyword-only, and **kwargs.
# Demonstrate how each type works.

# Solution:
# order: positional, default, *args, keyword-only (after *args), **kwargs
def full_function(pos1, pos2, default_val="default", *args, keyword_only="kw_default", **kwargs):
    print(f"Positional 1:    {pos1}")
    print(f"Positional 2:    {pos2}")
    print(f"Default value:   {default_val}")
    print(f"Extra *args:     {args}")
    print(f"Keyword-only:    {keyword_only}")
    print(f"Extra **kwargs:  {kwargs}")
    print()

# Call with minimum args
print("--- Minimum call ---")
full_function("A", "B")

# Call with all types
print("--- Full call ---")
full_function("X", "Y", "custom", 1, 2, 3,
              keyword_only="provided",
              option1=True, option2=42)

# Example Output:
# Positional 1:    A
# Positional 2:    B
# Default value:   default
# Extra *args:     ()
# Keyword-only:    kw_default
# Extra **kwargs:  {}
