"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day07_ranges.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

print(range(10))
print(list(range(10)))
print(range(0, 9, 2) == range(0, 10, 2))

even = range(10,0,-2)
odd = range(9,0,-2)
print("The even range is {} and the values are {}".format(even, list(even)))
print("The odd range is {} and the values are {}".format(odd, list(odd)))

val = int(input("Please provide a whole number for the divisibility check: "))
request = int(input("Please provide a whole number, less than 1 million, that is to be tested for divisibility: "))
in_range = range(val, 1000000, val)
if request > 1000000:
      print("Please select a number less than 1 million and try again. Thank you")
elif request in in_range:
      print("{} is divisible by {}.".format(request, val))
else:
      print("{} is not divisible by {}.".format(request, val))