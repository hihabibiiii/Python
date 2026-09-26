# Question: Take a multi-line string, use splitlines() to get individual lines,
#           then process each line (strip and print with a line number).
# Example:
#   Multi-line string -> splitlines() -> process each line

multi_line = """  Line one: Python is great.
  Line two: Learning is fun.
  Line three: Practice makes perfect.  
  Line four: Keep going!  """

lines = multi_line.splitlines()
print(f"Total lines: {len(lines)}")
print("\nProcessed lines (stripped):")
for i, line in enumerate(lines, start=1):
    processed = line.strip()
    print(f"  Line {i}: {processed}")
