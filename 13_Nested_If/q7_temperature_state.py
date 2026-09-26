# Question:
# Take a temperature in Celsius from the user.
# If temperature > 0:
#   - If temperature > 100: print 'Boiling point! Very hot.'
#   - Else: print 'Warm (above freezing).'
# If temperature <= 0:
#   - If temperature == 0: print 'Exactly at freezing point.'
#   - Else: print 'Below freezing! Very cold.'
#
# Example:
#   Input: 150  -> Boiling point! Very hot.
#   Input: 25   -> Warm (above freezing).
#   Input: 0    -> Exactly at freezing point.
#   Input: -10  -> Below freezing! Very cold.

temperature = float(input("Enter the temperature in Celsius: "))

if temperature > 0:
    if temperature > 100:
        print("Boiling point! Very hot.")
    else:
        print("Warm (above freezing).")
else:
    if temperature == 0:
        print("Exactly at freezing point.")
    else:
        print("Below freezing! Very cold.")
