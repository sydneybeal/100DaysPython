import random
import turtle
import webbrowser
import time
from datetime import datetime
import os

"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day18_packages.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

# for func in dir(__builtins__):
#     print(func)
#
#
# num = random.randint(0, 100)
# for i in range(0, 3):
#    try:
#        guess = int(input("Guess a number between 0 and 100: "))
#    except:
#        print("Please enter a valid integer between 0 and 100.")
#        break
#    if guess == num:
#        print("{} is the correct value. You win.".format(guess))
#    elif guess < num:
#        print("{} is lower than the value. You have {} tries left.".format(guess, 2 - i))
#    elif guess > num:
#        print("{} is higher than the value. You have {} tries left.".format(guess, 2 - i))
#    else:
#        print("Something went wrong.")

# jonathan = turtle.Turtle()
# jonathan.shape("turtle")
# jonathan.forward(100)
# jonathan.right(90)
# jonathan.forward(100)
# jonathan.right(90)
# jonathan.forward(100)
# jonathan.right(90)
# jonathan.forward(100)
# turtle.done()

# import webbrowser
# webbrowser.open("https://docs.python.org/3/library/webbrowser.html")
#chrome = webbrowser.get(using='google-chrome')
#chrome.open_new("https://www.youtube.com/watch?v=CMNry4PE93Y")
#help(webbrowser)

# start = time.time()
# print("Program Start")
# time.sleep(5)
# print("Program End. The total execution time was {} sec.".format(time.time() - start))


print(datetime.today())
print("Day: {}\nMonth: {}\nYear: {}".format(datetime.today().day, datetime.today().month, datetime.today().year))
if datetime.today() > datetime(datetime.today().year, 7, 4):
    days_until = (datetime(datetime.today().year + 1, 7, 4) - datetime.today()).days
    age = (datetime.today().year + 1) - 1776
else:
    days_until = (datetime(datetime.today().year, 7, 4) - datetime.today()).days
    age = datetime.today().year - 1776
print("There are {} days left until MURICA's birthday. MURICA will be {} years old.".format(days_until, age))

import os
print(os.getcwd())
print(os.cpu_count())
print(os.getlogin())