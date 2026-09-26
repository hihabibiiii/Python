# Question: Take a list of exam scores (assumed already sorted in ascending order),
#           slice the top 5 scores.
# Top 5 = last 5 elements when sorted ascending.
# Example:
#   Scores (sorted): [45, 55, 62, 68, 72, 78, 85, 90, 95, 98]
#   Top 5: [78, 85, 90, 95, 98]

scores = [45, 55, 62, 68, 72, 78, 85, 90, 95, 98]
print("All scores (sorted ascending):", scores)

top_5 = scores[-5:]
print("Top 5 scores:", top_5)
print("Highest score:", top_5[-1])
