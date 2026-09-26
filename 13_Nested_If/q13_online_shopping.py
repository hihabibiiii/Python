# Question:
# Simulate an online shopping cart using nested if.
# Step 1: If cart_total > 0 (cart is not empty):
#   Step 2: If cart_total >= 500 (free shipping threshold):
#     - Print 'Free shipping applied!'
#     Step 3: If user is a premium member:
#       - Apply an extra 10% discount and show the final price.
#     - Else: no extra discount.
#   Else (cart_total < 500): print 'Shipping charges: 50'
# Else: print 'Your cart is empty.'
#
# Example:
#   total=600, premium=yes -> Free shipping + extra discount
#   total=600, premium=no  -> Free shipping, no extra discount
#   total=300              -> Shipping charges: 50
#   total=0                -> Your cart is empty.

cart_total = float(input("Enter your cart total: "))

if cart_total > 0:
    if cart_total >= 500:
        print("Free shipping applied!")
        is_premium = input("Are you a premium member? (yes/no): ").lower()
        if is_premium == "yes":
            discount = cart_total * 0.10
            final_price = cart_total - discount
            print(f"Extra 10% premium discount: -{discount:.2f}")
            print(f"Final price: {final_price:.2f}")
        else:
            print(f"Final price: {cart_total:.2f}")
    else:
        print("Shipping charges: 50")
        print(f"Final price: {cart_total + 50:.2f}")
else:
    print("Your cart is empty.")
