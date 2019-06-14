"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day13_continueBreak.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed " \
             "Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! " \
             "Who's with me? Let's go!"
output = ""
for letter in motivation:
   if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
      output += letter
print(output)

motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed " \
             "Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! " \
             "Who's with me? Let's go!"
output = ""
for letter in motivation:
   if letter.lower() not in 'bcdfghjklmnpqrstvwxyz':
      continue
   else:
      output += letter
print(output)


motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed " \
             "Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! " \
             "Who's with me? Let's go!"
output = ""

for letter in motivation:
   if letter.lower() in 'abcdefghijklmnopqrstuvwxyz':
      output += letter
   else:
      break
print(output)

motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed " \
             "Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! " \
             "Who's with me? Let's go!"
output = ""
for letter in motivation:
   if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
      output += letter
print(output)

