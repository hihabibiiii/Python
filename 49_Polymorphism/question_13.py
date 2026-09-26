# Question:
# Create a Payment base class and subclasses: CreditCard, Cash, UPI.
# Each has a process() method that behaves differently.

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        return f"Processing payment of ${self.amount:.2f}"

class CreditCard(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number[-4:]  # Last 4 digits

    def process(self):
        return f"Credit Card ****{self.card_number}: Charging ${self.amount:.2f}"

class Cash(Payment):
    def process(self):
        return f"Cash Payment: Received ${self.amount:.2f}. Please give change if needed."

class UPI(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def process(self):
        return f"UPI ({self.upi_id}): Transferring ${self.amount:.2f}"

payments = [
    CreditCard(150.00, "4111111111111234"),
    Cash(50.00),
    UPI(75.50, "user@bank"),
]

print("Payment Processing:")
for p in payments:
    print(f"  {p.process()}")
