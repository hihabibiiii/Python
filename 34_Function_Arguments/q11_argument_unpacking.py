# Question 11 (Hard):
# Demonstrate argument UNPACKING: pass a list as *args and a dictionary as **kwargs
# to a function using the * and ** operators at the call site.

# Solution:
def introduce(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Normal call
introduce("Alice", 25, "Paris")

# Unpack a list as positional args
args_list = ["Bob", 30, "Berlin"]
introduce(*args_list)

# Unpack a dictionary as keyword args
kwargs_dict = {"name": "Carol", "age": 28, "city": "Tokyo"}
introduce(**kwargs_dict)

# Practical: combining both
def display_order(item, quantity, price, currency="USD"):
    print(f"Item: {item}, Qty: {quantity}, Price: {currency} {price:.2f}")

order_args = ("Apple", 3)
order_kwargs = {"price": 1.50, "currency": "EUR"}
display_order(*order_args, **order_kwargs)

# Example Output:
# Name: Alice, Age: 25, City: Paris
# Name: Bob, Age: 30, City: Berlin
# Name: Carol, Age: 28, City: Tokyo
# Item: Apple, Qty: 3, Price: EUR 1.50
