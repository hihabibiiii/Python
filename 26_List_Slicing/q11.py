# Question: Split a list of 12 months into four quarters using slicing.
# Q1: months[0:3], Q2: months[3:6], Q3: months[6:9], Q4: months[9:12]

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

print("All months:", months)
print()

q1 = months[0:3]
q2 = months[3:6]
q3 = months[6:9]
q4 = months[9:12]

print("Q1 (Jan-Mar):", q1)
print("Q2 (Apr-Jun):", q2)
print("Q3 (Jul-Sep):", q3)
print("Q4 (Oct-Dec):", q4)
