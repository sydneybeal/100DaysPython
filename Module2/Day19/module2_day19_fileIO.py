"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day19_fileIO.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

import this
import os

print(os.getcwd())
os.chdir('/Users/sydneybeal/Documents/repos/100DaysPython/Module2/Day19/')

zen = ""
for letter in list(this.s):
    if letter in list(this.d.keys()):
        zen += this.d[letter]
    else:
        zen += letter
print(zen)

with open('zen.txt', 'w') as z:
    z.write(zen)
z.close()

with open('declaration.txt', 'r') as d:
    print(d.readline())
    print(d.readline(25))
d.close()

with open('declaration.txt', 'r') as d:
    for lines in d:
        print(lines, end='')
d.close()

# Read the file in the original state.
print("\n\n")
print("{:=^50}\n".format(" BEFORE APPEND "))
with open('constitution.txt', 'r') as c:
    for lines in c:
        print(lines, end='')
c.close()

# Appending action
with open('constitution.txt', 'a') as c:
    print('\n', file=c)
    with open('billofrights.txt', 'r') as b:
        for lines in b:
            print(lines, end='', file=c)
    b.close()
c.close()

# Confirmation of successful appending.
print("\n\n")
print("\n\n{:=^50}\n".format(" AFTER APPEND "))
with open('constitution.txt', 'r') as c:
    for lines in c:
        print(lines, end='')
c.close()