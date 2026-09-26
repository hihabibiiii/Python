# Question:
# Chain all three: map(), filter(), and reduce().
# From a list of strings:
#   1. filter() - keep non-empty strings
#   2. map() - convert each to its length
#   3. reduce() - sum all lengths (total characters)

from functools import reduce

strings = ["hello", "", "world", "python", "", "is", "fun", ""]
print(f"Strings: {strings}")

# Step 1: Filter non-empty strings
non_empty = filter(lambda s: len(s) > 0, strings)

# Step 2: Map to lengths
lengths = map(lambda s: len(s), non_empty)

# Step 3: Reduce to total
total_chars = reduce(lambda x, y: x + y, lengths)

print(f"Total characters (excluding empty strings): {total_chars}")
