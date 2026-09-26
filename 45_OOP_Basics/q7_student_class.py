# Question: Create a class Student with name and marks list, and a method average().

# Example output:
# Student: Alice
# Marks: [85, 92, 78, 90, 88]
# Average: 86.60
# Highest: 92
# Lowest: 78

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def highest(self):
        return max(self.marks)

    def lowest(self):
        return min(self.marks)

    def display(self):
        print(f"Student: {self.name}")
        print(f"Marks:   {self.marks}")
        print(f"Average: {self.average():.2f}")
        print(f"Highest: {self.highest()}")
        print(f"Lowest:  {self.lowest()}")

# Create student objects
s1 = Student("Alice", [85, 92, 78, 90, 88])
s1.display()

print()

s2 = Student("Bob", [70, 65, 80, 75, 60])
s2.display()
