# Question 4 (Easy):
# Take a student's mark from the user.
# Check if the mark is >= 50 (passing mark).
# Print whether the student passed or failed.

# Solution:
mark = float(input("Enter your mark: "))

if mark >= 50:
    print(f"Mark: {mark} — PASSED (>= 50)")
else:
    print(f"Mark: {mark} — FAILED (< 50)")

# Example:
# Mark: 65 — PASSED
# Mark: 43 — FAILED
