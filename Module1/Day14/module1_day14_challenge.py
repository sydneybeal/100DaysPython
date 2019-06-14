"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day14_challenge.py
    Creation Date:  <REPLACE>
    Description:    Create a program that iterates through a list of values. If the object is immutable, print the type
                    and advance to the next step. If the object is mutable and a string, add "Allegedly" to the end. If
                    the object is mutable and a number, take 10 (for an int) to 20 (for a float) percent off, print the
                    new value, and overwrite the value in the existing position. If an object is not a string, number,
                    or tuple, end the program immediately while displaying the object and the type for review.
"""

content = ["Wayne is the toughest guy in Letterkenny.", list(range(0,101,10)), ("Wayne", "Dan", "Katy", "Daryl"), 10.4]

for i in content:
    # print(type(i))
    if type(i) == tuple:
        print("Object is immutable and is type {0}".format(type(i)))
    else:
        # print("Object is mutable\n")
        if type(i) == str:
            i += " Allegedly."
            print(i)
        elif type(i) == float:
            i *= 0.8
            print(i)
        elif type(i) == int:
            i *= 0.9
            print(i)
        else:
            print("Object: [{0}] is type {1}".format(i, type(i)))