# Question: Chain multiple string methods to clean and format user input.
# Steps:
#   1. strip()  -> remove leading/trailing whitespace
#   2. lower()  -> convert to lowercase
#   3. replace spaces with underscores
#   4. Remove special characters (keep only alphanumeric and underscores) using a loop
# Example:
#   Input:  "  Hello, World! 2024  "
#   Output: hello_world_2024

raw_input = input("Enter a string to clean: ")

# Step 1: Strip whitespace
step1 = raw_input.strip()
print("After strip():", step1)

# Step 2: Convert to lowercase
step2 = step1.lower()
print("After lower():", step2)

# Step 3: Replace spaces with underscores
step3 = step2.replace(" ", "_")
print("After replacing spaces:", step3)

# Step 4: Remove special characters (keep only letters, digits, underscores)
step4 = ""
for char in step3:
    if char.isalnum() or char == "_":
        step4 += char

print("After removing special chars:", step4)
print("\nFinal cleaned output:", step4)
