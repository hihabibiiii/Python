# Question: Take a date string in 'YYYY-MM-DD' format and extract the year, month,
#           and day using slicing.
# Example:
#   Input: "2024-03-15"
#   Output: Year: 2024, Month: 03, Day: 15

date_str = input("Enter a date in YYYY-MM-DD format: ")
year = date_str[:4]
month = date_str[5:7]
day = date_str[8:10]
print("Year:", year)
print("Month:", month)
print("Day:", day)
