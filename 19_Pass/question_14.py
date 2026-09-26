# Question:
# Create an if/elif/else chain where one branch is intentionally a no-op (pass).
# Classify a traffic light color and act accordingly.
# Yellow light = pass (no specific action, just wait).

light = input("Enter traffic light color (red/yellow/green): ").strip().lower()

if light == "red":
    print("Stop the vehicle.")
elif light == "yellow":
    pass  # Intentional no-op: just wait, no specific action needed
elif light == "green":
    print("Go! Proceed safely.")
else:
    print("Unknown signal. Be cautious.")

print("Signal processed.")
