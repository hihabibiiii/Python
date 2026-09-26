# Question:
# Create a lambda that accepts *args and returns their sum.
# Test it with different numbers of arguments.

sum_all = lambda *args: sum(args)

print(f"sum_all(1, 2, 3)       = {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20)        = {sum_all(10, 20)}")
print(f"sum_all(1,2,3,4,5,6,7) = {sum_all(1,2,3,4,5,6,7)}")
