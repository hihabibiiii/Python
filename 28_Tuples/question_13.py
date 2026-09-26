# Question:
# Given two lists: names and scores.
# Zip them into a list of tuples.
# Then "unzip" back into two separate lists using zip(*...).

names = ["Alice", "Bob", "Charlie", "Diana"]
scores = [85, 92, 78, 95]

# Zip into list of tuples
paired = list(zip(names, scores))
print(f"Paired (zipped): {paired}")

# Unzip back
names_back, scores_back = zip(*paired)
names_back = list(names_back)
scores_back = list(scores_back)

print(f"Names recovered:  {names_back}")
print(f"Scores recovered: {scores_back}")
