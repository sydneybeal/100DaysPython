# Day 1: Installing Python
**Completion Date:** 31 May 2019

**Learned:**
How to connect Github to PyCharm

# Day 2: Printing in Python
**Completion Date:** 3 Jun 2019

**Learned:**
String/integer concatenation
String replacement doesn't need numbers in {}
f-strings

# Day 3: Operators
**Completion Date:** 3 Jun 2019

**Learned:**
Difference between single, double, triple quotes
printing raw strings

# Day 4: Variables & Variable Types
**Completion Date:** 4 Jun 2019

**Learned:**
Can overwrite a variable with different data type
How to print data type of a var

# Day 5: String Formatting
**Completion Date:** 4 Jun 2019

**Learned:** 
Casing
Justification of printed strings and variables
Padding
Float precision

# Day 6: Lists
**Completion Date:** 6 Jun 2019

**Learned:** 
transformations to variables of lists also apply to the original
instantiate a list off the original to keep them separate (new_list=list(original_list))
combining lists with + or extend(list)
sort using .sort() or sorted(list)
printing the index prints only the first instance
pop the last item or specified index
items can be changed

# Day 7: Ranges
**Completion Date:** 6 Jun 2019

**Learned:**
steps in ranges
complex way of testing divisibility

# Day 8: Tuples
**Completion Date:** 7 Jun 2019

**Learned:**
tuples have static items, cannot be changed, good for metadata etc that should not be changed
instantiated by comma separated list, either with or without parentheses
accessing elements in tuples and putting into variables
can modify element of a list inside of a tuple

# Day 9: Index and Slicing
**Completion Date:** 10 Jun 2019

**Learned:**
can slice variables
can make a variable out of slicing another list or variable

# Day 10: If/Else
**Completion Date:** 10 Jun 2019

**Learned:** 
nested if/else statements, nested inputs
ternary operator

# Day 11: Augmented Assignments
**Completion Date:** 11 Jun 2019

**Learned:** 
Adding strings together with augmented assignments
floor operator
shift operators
and/or operators
multiplicative string concatenation

# Day 12: Loops
**Completion Date:** 13 Jun 2019

**Learned:** 
Formatting (indentation, etc) is important
input in loops
difference between while and for - while does not iterate automatically

# Day 13: Continue/Break
**Completion Date:** 13 Jun 2019

**Learned:**
continue just means move to the next step
break gets out of the current loop being executed


# Day 14: Module 1 Challenge
**Completion Date:** 14 Jun 2019

**Learned:** 
equality testing for variable type (just "== int", "== str", etc)
elif for testing sequence of things

# Day 15: Dictionaries
**Completion Date:** 17 Jun 2019

**Learned:**
one key can have a list of values that can be retrieved by slicing
can add keys in any order
comparing dictionaries
accessing list of keys and values
accessing key in a tuple, accessing values by tuple slicing or lookup by key
default values for incorrect keys or pre-set information

# Day 16: Sets
**Completion Date:** 17 Jun 2019

**Learned:**
creating sets with {} or keyword "sets"
mutable and iterable
determining the different or overlapping elements
.difference_update(<other set>) removes elements that are already in other set with no output, changes the set
.symmetric_difference(<other set>) returns elements unique to one of the sets, does not change the set
.symmetric_difference_update(<other set>) does the same but changes the set
sorting, removing, discarding (remove throws error, discard does not), use try and except for "remove"
frozenSet cannot be modified, immutable
.clear() to empty the set

# Day 17: User Input
**Completion Date:** 18 Jun 2019

**Learned:** 
storing input in variable
interactive input with conditional statements comparing strings

# Day 18: Packages
**Completion Date:** 18 Jun 2019

**Learned:** 
determining all the builtins
standard library packages can be imported at the top with an import statement, without having to install them (e.g. random)
turtle package brings up its own gui
opening web browsers and finding help
time.time(), datetime
interacting with filesystem
installing extra packages with pip

# Day 19: File Input/Output
**Completion Date:** 19 Jun 2019

**Learned:** 
printing working directory/change directory
nested file opening/appending

# Day 20: Functions
**Completion Date:** 20 Jun 2019

**Learned:** 
blank lines before and after function
need to be defined before can be called
calling functions from other other functions
docstrings and .__doc__ object
typestrings for autocomplete hints and docstring details

# Day 21: Pytest
**Completion Date:** 21 Jun 2019

**Learned:** 
setting up configuration to run pytests

# Day 22: Recursive Functions
**Completion Date:** 28 Jun 2019

**Learned:** 
Fibonacci of 20000 is a very very long number
Was able to execute higher than the recursion limit on cached recursion but not regular recursion

# Day 23: Lambdas
**Completion Date:** 28 Jun 2019

**Learned:** 
getting into the habit of writing with few lines makes you a more efficient and creative Python problem solver
lambda is simpler and shorter but more limited in functionality than regular functions - multiway comparisons, docstrings, etc

# Day 24: Object Oriented Python
**Completion Date:** 28 Jun 2019

**Learned:** 
Python pillars are app development, data science, and web development - OOP falls under app development
Decorators "wrap" functions - can pass a function as a param to another function, extends the behavior of the higher up function w/o changing it
Inner functions are defined inside other functions, if they are defined by another variable they can be accessed
Decorators can be over-complicated, but classes help keep code simple and have more functionality than tuples and dictionaries

# Day 25: List Comprehensions
**Completion Date:** 30 Jun 2019

**Learned:**
Shorter way to create lists
accessing tuple elements in list comprehensions

# Day 26: Map, Filter, and Zip
**Completion Date:** 30 Jun 2019

**Learned:** 
lambdas and filters can be used to create and print complicated lists all with one line of code
zipping combines elements from several lists into one big object
reduce() exists but is irrelevant

# Day 27: Logging
**Completion Date:** 30 Jun 2019

**Learned:** 
logger.setLevel("INFO") changes the level of logging
logs can be formatted
filemode="w" switches it from append mode to overwrite mode
logging can show explicit inputs and outputs from functions and what is actually occuring


# Day 28: Module 2 Challenge
**Completion Date:** 12 July 2019

**Learned:**
stacked loops for user input
looping through dictionaries and matching to input letters
incorporating logging throughout a program
encrypting and decrypting phrases

# Day 29: File Manipulations
**Completion Date:** 12 July 2019

**Learned:**
os.listDir() function to get list of file names
splitting file names from extensions, and splitting by a specified delimiter
padding to sort correctly
renaming files

# Day 30: File Search
**Completion Date:** 12 July 2019

**Learned:** 
Walking through files in a directory
Searching vast range of documents for a single phrase of text
Loading up search lines and looping through the enumeration

# Day 31: CSV Manipulations
**Completion Date:** 12 July 2019

**Learned:** 
opening CSVs in overwrite or append mode
commas can be included if string is in quotes
CSVs are type agnostic
Using read mode and secondary file to check if a record exists before entering

# Day 32: Excel Manipulations
**Completion Date:** 14 July 2019

**Learned:**
opening and manipulating excel documents in Python
storing data from excel docs into variables
using loops to automate excel data entry

# Day 33: PDF Manipulations
**Completion Date:** 14 July 2019

**Learned:** 
Using tabula to read a pdf and write all to a temp file
Cleaning input data of extraneous lines, null columns, etc

# Day 34: PowerPoint Manipulations
**Completion Date:** 14 July 2019

**Learned:**
Storing all information from a powerpoint into a Python object
Storing and manipulating elements from each slide
Automatically generating and writing to a PPT file

# Day 35: Task Scheduler
**Completion Date:** 14 July 2019

**Learned:** 
locating python executable with print sys.executable
different operating systems have different methods for opening files
setting a timer to launch a specific file in its default application
system scheduler can be paired with python to automate boot-up or create timed sequences

# Day 36: Email/SMS Notifications
**Completion Date:** 14 July 2019

**Learned:** 
Setting gmail settings to allow unsecure apps to log in with my credentials
Automatically sending email notifications

# Day 37: Mouse/Keyboard Manipulations
**Completion Date:** 

**Learned:** 

# Day 38: Web Automation
**Completion Date:** 

**Learned:** 

# Day 39: Stock Market Data Collection
**Completion Date:** 

**Learned:** 

# Day 40: Image Manipulations
**Completion Date:** 

**Learned:** 

# Day 41: Creating a Chatbot
**Completion Date:** 

**Learned:** 

# Day 42: Module 3 Challenge
**Completion Date:** 

**Learned:** 

# Day 43: _Topic_
**Completion Date:** 

**Learned:** 

# Day 44: _Topic_
**Completion Date:** 

**Learned:** 

# Day 45: _Topic_
**Completion Date:** 

**Learned:** 

# Day 46: _Topic_
**Completion Date:** 

**Learned:** 

# Day 47: _Topic_
**Completion Date:** 

**Learned:** 

# Day 48: _Topic_
**Completion Date:** 

**Learned:** 

# Day 49: _Topic_
**Completion Date:** 

**Learned:** 

# Day 50: _Topic_
**Completion Date:** 

**Learned:** 

# Day 51: _Topic_
**Completion Date:** 

**Learned:** 

# Day 52: _Topic_
**Completion Date:** 

**Learned:** 

# Day 53: _Topic_
**Completion Date:** 

**Learned:** 

# Day 54: _Topic_
**Completion Date:** 

**Learned:** 

# Day 55: _Topic_
**Completion Date:** 

**Learned:** 

# Day 56: Module 4 Challenge
**Completion Date:** 

**Learned:** 

# Day 57: _Topic_
**Completion Date:** 

**Learned:** 

# Day 58: _Topic_
**Completion Date:** 

**Learned:** 

# Day 59: _Topic_
**Completion Date:** 

**Learned:** 

# Day 60: _Topic_
**Completion Date:** 

**Learned:** 

# Day 61: _Topic_
**Completion Date:** 

**Learned:** 

# Day 62: _Topic_
**Completion Date:** 

**Learned:** 

# Day 63: _Topic_
**Completion Date:** 

**Learned:** 

# Day 64: _Topic_
**Completion Date:** 

**Learned:** 

# Day 65: _Topic_
**Completion Date:** 

**Learned:** 

# Day 66: _Topic_
**Completion Date:** 

**Learned:** 

# Day 67: _Topic_
**Completion Date:** 

**Learned:** 

# Day 68: _Topic_
**Completion Date:** 

**Learned:** 

# Day 69: _Topic_
**Completion Date:** 

**Learned:** 

# Day 70: Module 5 Challenge
**Completion Date:** 

**Learned:** 

# Day 71: _Topic_
**Completion Date:** 

**Learned:** 

# Day 72: _Topic_
**Completion Date:** 

**Learned:** 

# Day 73: _Topic_
**Completion Date:** 

**Learned:** 

# Day 74: _Topic_
**Completion Date:** 

**Learned:** 

# Day 75: _Topic_
**Completion Date:** 

**Learned:** 

# Day 76: _Topic_
**Completion Date:** 

**Learned:** 

# Day 77: _Topic_
**Completion Date:** 

**Learned:** 

# Day 78: _Topic_
**Completion Date:** 

**Learned:** 

# Day 79: _Topic_
**Completion Date:** 

**Learned:** 

# Day 80: _Topic_
**Completion Date:** 

**Learned:** 

# Day 81: _Topic_
**Completion Date:** 

**Learned:** 

# Day 82: _Topic_
**Completion Date:** 

**Learned:** 

# Day 83: _Topic_
**Completion Date:** 

**Learned:** 

# Day 84: Module 6 Challenge
**Completion Date:** 

**Learned:** 

# Day 85: _Topic_
**Completion Date:** 

**Learned:** 

# Day 86: _Topic_
**Completion Date:** 

**Learned:** 

# Day 87: _Topic_
**Completion Date:** 

**Learned:** 

# Day 88: _Topic_
**Completion Date:** 

**Learned:** 

# Day 89: _Topic_
**Completion Date:** 

**Learned:** 

# Day 90: _Topic_
**Completion Date:** 

**Learned:** 

# Day 91: _Topic_
**Completion Date:** 

**Learned:** 

# Day 92: _Topic_
**Completion Date:** 

**Learned:** 

# Day 93: _Topic_
**Completion Date:** 

**Learned:** 

# Day 94: _Topic_
**Completion Date:** 

**Learned:** 

# Day 95: _Topic_
**Completion Date:** 

**Learned:** 

# Day 96: _Topic_
**Completion Date:** 

**Learned:** 

# Day 97: _Topic_
**Completion Date:** 

**Learned:** 

# Day 98: Module 7 Challenge
**Completion Date:** 

**Learned:** 

# Day 99: Capstone
**Completion Date:** 

**Learned:** 

# Day 100: Capstone
**Completion Date:** 

**Learned:** 
