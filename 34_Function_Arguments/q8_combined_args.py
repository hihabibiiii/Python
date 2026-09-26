# Question 8 (Medium):
# Define a function that combines: positional arguments, a default argument,
# and *args. Show how they work together.

# Solution:
def describe(title, category="General", *details):
    print(f"Title:    {title}")
    print(f"Category: {category}")
    if details:
        print(f"Details:  {', '.join(str(d) for d in details)}")
    else:
        print("Details:  None provided")
    print()

# Positional only
describe("Python Course")

# With category
describe("Data Science", "Tech")

# With category and extra details
describe("Machine Learning", "AI", "Beginner", "3 months", "Certificate")

# Example Output:
# Title:    Python Course
# Category: General
# Details:  None provided
#
# Title:    Data Science
# Category: Tech
# Details:  None provided
#
# Title:    Machine Learning
# Category: AI
# Details:  Beginner, 3 months, Certificate
