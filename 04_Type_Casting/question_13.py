# Question 13 (Hard):
# Take the string '1,2,3,4,5'.
# Split it by commas, convert each element to an integer,
# then compute and print the sum and average.

# Solution:
data = '1,2,3,4,5'
parts = data.split(',')       # ['1', '2', '3', '4', '5']

total = 0
count = 0
for part in parts:
    total = total + int(part)
    count = count + 1

average = total / count

print("Data string :", data)
print("As integers :", [int(p) for p in parts])
print("Sum         :", total)
print("Average     :", average)

# Output:
# Data string : 1,2,3,4,5
# As integers : [1, 2, 3, 4, 5]
# Sum         : 15
# Average     : 3.0
