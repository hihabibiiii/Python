# Question 15 (Hard):
# Create a mini scope quiz program.
# Ask the user multiple-choice questions about Python scope.
# Display the answer and explanation after each question.

# Solution:
questions = [
    {
        "q": "Q1: What is the scope of a variable defined inside a function?",
        "options": ["A) Global", "B) Local", "C) Built-in", "D) Enclosing"],
        "answer": "B",
        "explanation": "Variables defined inside a function have LOCAL scope."
    },
    {
        "q": "Q2: Which keyword allows modifying a global variable inside a function?",
        "options": ["A) nonlocal", "B) extern", "C) global", "D) public"],
        "answer": "C",
        "explanation": "The 'global' keyword declares that you want to modify the global variable."
    },
    {
        "q": "Q3: In LEGB, what does 'E' stand for?",
        "options": ["A) External", "B) Enclosed", "C) Enclosing", "D) Evaluated"],
        "answer": "C",
        "explanation": "E = Enclosing scope (scope of any enclosing functions)."
    },
    {
        "q": "Q4: Which keyword modifies a variable in an enclosing (not global) scope?",
        "options": ["A) global", "B) outer", "C) enclosing", "D) nonlocal"],
        "answer": "D",
        "explanation": "'nonlocal' refers to the nearest enclosing scope, not global."
    },
    {
        "q": "Q5: Can a for-loop variable be accessed after the loop in Python?",
        "options": ["A) Yes", "B) No"],
        "answer": "A",
        "explanation": "Python for-loop variables persist in the enclosing scope after the loop."
    }
]

score = 0
print("=== Python Scope Quiz ===\n")

for item in questions:
    print(item["q"])
    for opt in item["options"]:
        print(" ", opt)
    answer = input("Your answer: ").strip().upper()
    if answer == item["answer"]:
        print("  CORRECT!")
        score += 1
    else:
        print(f"  WRONG! Correct answer: {item['answer']}")
    print(f"  Explanation: {item['explanation']}\n")

print(f"Final Score: {score}/{len(questions)}")
