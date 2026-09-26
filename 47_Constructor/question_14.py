# Question:
# Create alternative constructors using class methods (@classmethod).
# A Date class with from_string() and from_tuple() class methods.

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str):
        """Alternative constructor: 'YYYY-MM-DD' format."""
        year, month, day = date_str.split("-")
        return cls(int(year), int(month), int(day))

    @classmethod
    def from_tuple(cls, date_tuple):
        """Alternative constructor: (year, month, day) tuple."""
        return cls(*date_tuple)

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

# Normal constructor
d1 = Date(2024, 3, 15)
print(f"From direct params: {d1}")

# Alternative constructor
d2 = Date.from_string("2024-07-04")
print(f"From string:        {d2}")

d3 = Date.from_tuple((2024, 12, 25))
print(f"From tuple:         {d3}")
