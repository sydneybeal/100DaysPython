"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day04_variables.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

greeting = "Hello"
_name = "General Kenobi."
Greeting = "There"
_bestLine_ep3_ = "You are a bold one."
print(greeting + " " + Greeting + "\n\t" + _name + " " + _bestLine_ep3_)
print("{} {}\n\t{} {}".format(greeting, Greeting, _name, _bestLine_ep3_))

released = 2005
print("Revenge of the Sith was released on May 4, " + str(released) + ".")
print("Revenge of the Sith was released on May 4, {}.".format(released))

a = 3
b = 4
c = a ** 2 + b ** 2
print("Pythagorean Theorem: a^2 + b^2 = c^2, so when a = {} and b = {}, then c^2 = {}".format(a, b, c))

film = "Revenge of the Sith"
print("Sith" in film)
print("sith" in film)
print("sith" in film.lower())

var = "Variables are mutable"
print(type(var))
var = 3
print(type(var))
var = 3.5
print(type(var))
var = int(var)
print(type(var))
var = str(var)
print(type(var))
var = float(var)
print(type(var))
var = True
print(type(var))
