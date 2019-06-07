"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day05_strFormat.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

cheers = "where everybody knows YOUR name."
print(cheers.capitalize())
print(cheers.title())
print(cheers.lower())
print(cheers.upper())
print(cheers.swapcase())

print("norm".upper())

spinoff = "Frasier"
yr = 1993
print("The show {} was a spinoff of Cheers that first aired in {}".format(spinoff.upper(), yr))

i = 13
print("{0:3} squared is {1:4}.".format(i, i ** 2))
print("{0:3} squared is {1:<4}.".format(i, i ** 2))
print("{0:3} squared is {1:>4}.".format(i, i ** 2))
print("{0:3} squared is {1:^4}.".format(i, i ** 2))

msg = "END OF CODE"
print("{:=^50}".format(msg))

print("{:.5}".format(cheers.capitalize()))

pi = 22 / 7
print("Pi as a float is {0:f}, as a float with a precision of 2 is {0:.2f}".format(pi))
print("The answer to life, the universe, and everything is {0:d} as an integer, or {0:=^10d} as a padded and centered integer".format(42))

pi = 22 / 7
print(f"Pi as a float is {pi:f}, as a float with a precision of 2 is {pi:.2f}")
print(f"The answer to life, the universe, and everything is {42:d} as an integer, or {42:=^10d} as a padded and centered integer")