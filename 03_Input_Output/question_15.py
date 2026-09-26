# Question 15 (Hard):
# Simulate a simple bill printer.
# Take the name and price for 3 items from the user.
# Print a formatted bill with a total at the bottom.

# Solution:
print("===== Bill Entry =====")
item1 = input("Enter item 1 name: ")
price1 = float(input(f"Enter price of {item1}: "))

item2 = input("Enter item 2 name: ")
price2 = float(input(f"Enter price of {item2}: "))

item3 = input("Enter item 3 name: ")
price3 = float(input(f"Enter price of {item3}: "))

total = price1 + price2 + price3

print("\n========== BILL ==========")
print(f"{'Item':<15} {'Price':>8}")
print("-" * 25)
print(f"{item1:<15} ${price1:>7.2f}")
print(f"{item2:<15} ${price2:>7.2f}")
print(f"{item3:<15} ${price3:>7.2f}")
print("-" * 25)
print(f"{'TOTAL':<15} ${total:>7.2f}")
print("===========================")

# Example Input / Output:
# Enter item 1 name: Coffee
# Enter price of Coffee: 3.5
# Enter item 2 name: Sandwich
# Enter price of Sandwich: 6.75
# Enter item 3 name: Juice
# Enter price of Juice: 2.0
#
# ========== BILL ==========
# Item              Price
# -------------------------
# Coffee            $  3.50
# Sandwich          $  6.75
# Juice             $  2.00
# -------------------------
# TOTAL             $ 12.25
# ===========================
