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