"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day11_augAssign.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

# += : Addition
# -= : Subtraction
# *= : Multiplication
# /= : Division
# //= : Floor Division
# %= : Remainder/Modulus
# **= : Exponent
# <<= : Left Shift
# >>= : Right Shift
# &= : And
# ^= : Exclusive Or (XOR)
# |= : Inclusive Or (OR)

x = 42
x += 3
print(x)

x = 42
x -= 3
print(x)

x = 42
x *= 3
print(x)

x = 42
x /= 3
print(x)

x = 42
x //= 3
print(x)

x = 42
x %= 3
print(x)

x = 42
x **= 3
print(x)

x = 1
x <<= 2
print(x)

x = 4
x >>= 1
print(x)

x = True
y = False
x &= y
print(x)

x = True
y = False
x ^= y
print(x)

x = True
y = False
x |= y
print(x)

x = "Ten Million "
y = "Dollars"
x *= 3
x += y
print(x)