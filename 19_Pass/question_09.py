# Question:
# Demonstrate the DIFFERENCE between pass and continue.
# Both seem to "skip" but they behave differently.
# pass: does nothing, loop continues normally.
# continue: skips the rest of THIS iteration, moves to next.

print("--- Using PASS ---")
for i in range(1, 6):
    if i == 3:
        pass  # Does nothing; print below still executes
    print(f"pass loop: i = {i}")

print()
print("--- Using CONTINUE ---")
for i in range(1, 6):
    if i == 3:
        continue  # Skips the rest; print below does NOT execute for i=3
    print(f"continue loop: i = {i}")
