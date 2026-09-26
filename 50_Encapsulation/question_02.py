# Question:
# Use a getter method to access a private attribute.

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    # Getter methods
    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

acc = BankAccount("Alice", 5000.0)

print(f"Owner:   {acc.get_owner()}")
print(f"Balance: ${acc.get_balance():,.2f}")
