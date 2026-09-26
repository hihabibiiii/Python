# Question:
# Create a class that tracks how many instances have been created.
# Use a class variable `count` and increment it in __init__.

class Robot:
    count = 0  # Class variable shared by all instances

    def __init__(self, name):
        Robot.count += 1
        self.name = name
        self.id = Robot.count
        print(f"Robot '{self.name}' created. Total robots: {Robot.count}")

    @classmethod
    def get_count(cls):
        return cls.count

# Create robots
r1 = Robot("Alpha")
r2 = Robot("Beta")
r3 = Robot("Gamma")

print(f"\nTotal robots created: {Robot.get_count()}")
print(f"r1.id={r1.id}, r2.id={r2.id}, r3.id={r3.id}")
