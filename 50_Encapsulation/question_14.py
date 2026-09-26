# Question:
# Create a Student class with a private marks list.
# Methods: add_mark(), get_average(), get_marks() (returns copy).
# No direct access to the internal list.

class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = []  # Private list

    def add_mark(self, mark):
        if not isinstance(mark, (int, float)):
            raise TypeError("Mark must be a number.")
        if not (0 <= mark <= 100):
            raise ValueError(f"Mark {mark} is out of range (0-100).")
        self.__marks.append(mark)

    def get_marks(self):
        return list(self.__marks)  # Return a COPY, not the original

    def get_average(self):
        if not self.__marks:
            return 0.0
        return sum(self.__marks) / len(self.__marks)

    def get_highest(self):
        return max(self.__marks) if self.__marks else None

    def __str__(self):
        return f"Student({self.name}, marks={self.__marks}, avg={self.get_average():.2f})"

s = Student("Alice")
s.add_mark(85)
s.add_mark(92)
s.add_mark(78)
s.add_mark(95)
print(s)

marks_copy = s.get_marks()
marks_copy.append(0)  # Modifying copy should NOT affect original
print(f"After modifying copy: {s.get_marks()}")  # Original unchanged

try:
    s.add_mark(105)
except ValueError as e:
    print(f"Error: {e}")
