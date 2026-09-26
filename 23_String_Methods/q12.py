# Question: Use zfill() to format numbers as fixed-width strings (e.g., '007').
# zfill(width) pads the string with leading zeros to reach the given width.
# Example:
#   Number: "7"   -> zfill(3) -> "007"
#   Number: "42"  -> zfill(5) -> "00042"

number = input("Enter a number: ")
width = int(input("Enter the desired total width: "))

formatted = number.zfill(width)
print(f"'{number}' formatted with zfill({width}): '{formatted}'")

# Practical example: format a list of agent IDs
print("\nPractical example - Agent IDs:")
agent_ids = [1, 5, 23, 100, 7]
for agent_id in agent_ids:
    print(f"  Agent: {str(agent_id).zfill(4)}")
