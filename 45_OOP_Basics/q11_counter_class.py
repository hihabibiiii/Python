# Question: Create a class Counter with count=0, methods increment(), decrement(), reset(), get_count().

# Example output:
# Initial count: 0
# After 3 increments: 3
# After 1 decrement: 2
# After reset: 0

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, by=1):
        self.count += by
        print(f"Incremented by {by}. Count: {self.count}")

    def decrement(self, by=1):
        self.count -= by
        print(f"Decremented by {by}. Count: {self.count}")

    def reset(self):
        self.count = 0
        print("Counter reset to 0.")

    def get_count(self):
        return self.count

# Test Counter
c = Counter()
print(f"Initial count: {c.get_count()}")

c.increment()
c.increment()
c.increment()
print(f"\nAfter 3 increments: {c.get_count()}")

c.decrement()
print(f"After 1 decrement: {c.get_count()}")

c.increment(5)
print(f"After increment by 5: {c.get_count()}")

c.reset()
print(f"After reset: {c.get_count()}")
