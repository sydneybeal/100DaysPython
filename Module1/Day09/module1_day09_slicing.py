"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day09_slicing.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

quotes = ["Pitter patter, let's get at 'er", "Hard no!", "H'are ya now?", "Good-n-you?", "Not so bad.", "Is that what you appreciates about me?"]
quotes[0]
print(f"{quotes[2]}\n\t{quotes[3]}\n{quotes[4]}")

print(quotes[2:5])

print(quotes[::5])

print(quotes[::-1])

print(quotes[0][::2])
print(quotes[0][::-1])

wayne = "Toughest Guy in Letterkenny"
print(wayne[::-1])

print("That's a Texas sized 10-4."[0:9:2])

print(quotes[:])
print(quotes[3:])
print(quotes[:3])
print(quotes[::3])

exchange = quotes[2:5]
print(exchange)