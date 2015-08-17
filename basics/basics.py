'''
Jennifer's cheat sheet for Python basic syntax and handy tips.
- Variables and basic operations
- Strings
- Console input
- Lists
- Tuples
- Control flow
- Functions
- Dictionaries
- Modules, namespaces and scripts
- Text file I/O
- Handy modules - date and time, random numbers
- Sorting
- IPython features
- Editor configuration
- Conventions and best practices

Each section of this cheatsheet can be copy/pasted into ipython (using the
%paste magic command for indented code) and run separately in an interactive
session.

Many of these code snippets are pilfered / adapted from Google's Python Class
(https://developers.google.com/edu/python/), the Python Tutorial
(https://docs.python.org/2/tutorial/) and codecademy.com.

A triple-quoted comment at the beginning of a module (.py)
file or function is automatically used as the documentation
string.
'''

print("\nWelcome to Jennifer's Python basics cheat sheet!")

def heading(s):
    '''Prints a nice heading to the console.'''
    line = '-' * 40
    print('\n' + line + '\n' + s + '\n' + line)

# ----------------------------------------------
# Variables and basic operations
# ----------------------------------------------

heading('Variables and basic operations')

print('''
Create a variable by assigning it a value, e.g.,
x = 10
No need to declare it as a variable of a certain type.
Python assigns it a type based on the value.

Avoid using the following variable names, which are
equal to built-in functions and would override them:
**** str, len, list, dict, map, filter ****

Basic math operators: +, -, *, /, **, %, //
Assignment operators: =, +=, -=, *=, /=, %=, **=, //=
Booleans:  True, False
Comparators: ==, !=, <, <=, >, >=
Boolean operators: and, or, not
''')

# Basic math operators
x = 72 + 23
x = 108 - 204
x = 108 * 0.5
x = 108 / 9
x = 2 ** 3 # Exponentiation
x = 4 % 3 # Modulus
x = 6 // 5 # Integer (floor) division

# Assignment operators
x1 = 10
x1 += 2 # Same as x1 = x1 + 2
x1 -= 5 # Same as x1 = x1 - 5
x1 *= 5 # Same as x1 = x1 * 2
x1 /= 7 # Same as x1 = x1 / 7
x1 %= 3 # Same as x1 = x1 % 3
x1 /= 4 # Same as x1 = x1 // 4

# Booleans and comparators
bool1 = True
bool2 = False
x1 = 10
x2 = 3
bool1 = x1 == x2
bool1 = x1 != x2
bool1 = x1 < x2
bool1 = x1 <= x2
bool1 = x1 > x2
bool1 = x1 >= x2

# Boolean operators
bool1 = (2 <= 2) and "Alpha" == "Bravo"
bool1 = (1<2) or (2<1)
bool1 = not (10>100)

# Type
print type(43) # int
print type(1.2) # float
print type('cat') # string

# ----------------------------------------------
# Strings
# ----------------------------------------------

heading('Strings')

# Single or double quotation marks:
str1 = "Cats say 'meow'."
str2 = 'Dogs say "woof".'

# Escape characters
str3 = 'Ford, you\'re turning into a penguin.  Stop it!'

# Multi-line strings
# --- With parentheses:
#     Doesn't include newlines unless added with \n
long1 = ("I can't keep track of her when she's *not* incorporeally possessing "
         "a space ship; don't look at me.")
# --- With triple quotation marks:
#     Include \ at end of line to exclude new line
long2 = """\
They say the snow on the roof is too heavy. \
They say the ceiling will cave in. \
His brains are in terrible danger.
Too... Much... Hair!
"""

print(long1)
print(long2)

# String methods
lunch = "Time is an illusion.  Lunchtime doubly so."
print(len(lunch))
print(lunch.lower())
print(lunch.upper())
pi = 3.14159
print(str(pi)) # Convert to string
s = str1 + " " + str2 # Concatenation
print(s)
s_exclaim = s.replace('.','!') # Replace substring
print(s_exclaim)
s_rep = 'kittens! ' * 3 # Repeats the string 'kittens! ' 3 times
print(s_rep)

# Indexing and slicing strings
'''
Indices start at 0 and count up, or from the end of the
string at -1 and count down.

Slicing: Extracting a range of indices (e.g., 1:4)
The slice n1:n2 is *inclusive* of n1 and *exclusive* of n2,
i.e. 1:4 gives elements 1,2,3.

There is no separate character type.  A character is a string
of size 1.
'''
s = 'Hello' # Indices: [0, 1, 2, 3, 4], and [-5, -4, -3, -2, -1]
print(s[0]) # 'H'
print(s[1:4]) # 'ell'
print(s[1:]) # 'ello'
print(s[-1]) # 'o'
print(s[:-3]) # 'He'
print(s[-3:]) # 'llo'
# Note: s[:n] + s[n:] is always equal to s

# Immutability
'''Strings are immutable in Python, i.e., you can't change individual
elements (you can only create a new string)'''
s = 'Cats'
print(s[0]) # 'C'
#s[0] = 'B' # Raises error
s = 'Bats' # Works

# Formatting strings
s1 = 'Cats'
s2 = 'world'
s3 = ("%s rule the %s.  Pi is %.2f to 2 digits." % (s1, s2, pi))
print(s3)

# ----------------------------------------------
# User input from console
# ----------------------------------------------

heading('User input from console')
print('Use raw_input(prompt)')

'''
name = raw_input('What is your name? ')
print('Hello %s!' %(name))
'''

# ----------------------------------------------
# Lists
# ----------------------------------------------

heading('Lists')

print('''
A list is a sequence of comma-separated values between [ ]
Lists and strings are both sequences, i.e. indexed by a range of integers
Lists usually homogeneous (e.g. [1, 4, 9, 20], ['cat', 'dog', 'hamster'])
Lists are mutable, so you can change individual elements

List methods: append, extend, insert, remove, pop, index,
count, sort, reverse
''')

# List assignment and operations
squares = [1, 4, 10, 16, 25]
print(squares[-3:]) # Slicing
squares[3] = 9 # Change individual elements
squares.append(36) # Append
squares.extend([49, 64]) # Extend
a = [-10, 3, 2] + [100, 200] # Concatenate
print(len(a)) # Length

# Membership testing
'''The "in" statement returns True if an element is in a list,
False if not.  And vice versa for "not in" statement '''
firefly = ['Mal', 'Wash', 'Zoe', 'Jayne', 'Kaylee', 'Inara', 'Simon',
    'River', 'Book']
test1 = 'Kaylee' in firefly # True
test2 = 'Sheldon' in firefly # False
test3 = 'Sheldon' not in firefly # True

# Deleting
# --- Use the del command to delete individual elements,
#     slices, empty the contents, or delete the list object
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0] # Now a is [1, 66.25, 333, 333, 1234.5]
del a[2:4] # Now a is [1, 66.25, 1234.5]
del a[:] # Now a is []
del a # Now a no longer exists

# Defining numeric lists
x1 = range(5) # 0, 1, 2, 3, 4
x2 = range(0, 10) # 0, 1, 2, 3, 4
x3 = range(0,10,2) # 0, 2, 4, 6, 8

# Sets
'''A set is an unordered collection with no duplicate elements'''
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print(basket)
print(fruit)

# Zip function for iterating over multiple lists
'''
zip will create pairs of elements when passed two lists, and will stop
at the end of the shorter list. zip can handle three or more lists as well.
'''
list_a = [3, 1, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a > b: print a
    else: print b

# ----------------------------------------------
# Tuples
# ----------------------------------------------

heading('Tuples')

print('''
A tuple is a sequence of comma-separated values between ( )
Tuples are usually heterogeneous (e.g. ('kitten', 2, False) )
Tuples are immutable, so you cannot change individual elements
Tuples can be used to return multiple values from a function

() can be ommited when assigning tuples, but must be included
when returning a tuple from a function
''')

# Tuple packing
t = 10, -12.34, 'hello'

# Tuple unpacking
x, y, z = t

print(t)
print(x)
print(y)
print(z)

# ----------------------------------------------
# Control flow
# ----------------------------------------------

heading('Control flow')

# If statements
# -------------
s = 'Curse your sudden but inevitable betrayal!'
if len(s) > 10:
    print('Long string')
elif len(s) < 5:
    print('Short string')
else:
    print('Medium string')

mylist = ['larry', 'curly', 'moe']
if 'curly' in mylist:
    print('Yay!')

# Any non-zero number tests as True
# Any list of non-zero length tests as True
# 0, None and [] test as False
x = 10
if x: print('Yes')
x = []
if x: print('Yes')
x = [0, 0, 0]
if x: print('Yes')

# For loops
# ---------
# Three methods for iterating over a list
animals = ["hamster", "rabbit", "cat", "gerbil"]

print("--- Loop over items:")
for item in animals:
	print("Hello " + item)

print("--- Loop over indices:")
for i in range(len(animals)):
    print(str(i) + ") " + animals[i])

print("--- Using enumerate()")
for i, anim in enumerate(animals):
    print(i, anim)

# List comprehension
# ------------------
strs = ['hello', 'and', 'goodbye']
myshout = [s.upper() for s in strs]
print(myshout)

squares = [x**2 for x in range(10)]
print(squares)

mylist = [(x,y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(mylist)

# While loops
# -----------
# Create a Fibonacci series up to n
n = 100
series = []
a, b = 0, 1
while a < n:
    series.append(a)
    a, b = b, a+b
print(series)

''' Additional control flow statements:
break - Breaks out of smallest enclosing for or while loop
continue - Continues with next iteration of loop
pass - Does nothing.  Use when syntax requires a statement but
       no action is needed.
'''

# ----------------------------------------------
# Functions
# ----------------------------------------------

heading('Functions')

# Defining functions
def shouting(s):
    '''
    Shouts a string in upper case with exclamation points!

    A triple-quoted comment at the beginning of the function
    (if present) is automatically used as the docstring.
    Convention: First line of docstring is a concise summary
    of the function.  If including additional lines, separate
    them from the first line with a blank second line.
    '''
    print("We're shouting!")
    return s.replace('.','!').upper() + '!!!'

print(shouting('Soft kitty. Warm kitty. Little ball of fur.'))

print('''
Indentation is Python's way of grouping elements.  An indented
line is not the same as a non-indented line, and the level of
indentation affects how the code is interpreted.  Recommended
indentation is 4 spaces per level.  You should configure your
text editor so that the Tab key gives 4 spaces.

To show function documentation (and object introspection) in ipython shell:
shouting? # Displays docstring and some other info
shouting?? # Displays source code, if feasible
help(shouting) # Displays detailed documentation
dir(shouting) # Displays list of attributes
''')

# Default argument values and keyword arguments
def my_pets(ncat, ndog=0, nhamster=0):
    print('I have %d cats, %d dogs, and %d hamsters!' % (ncat, ndog, nhamster))

my_pets(2)
my_pets(2, 1)
my_pets(2, nhamster=3)

'''
Notes:
Keyword arguments must follow positional arguments in a function call.

A function without a return expression returns None.
a = my_pets(2) # a is None

Use tuples to return multiple outputs, e.g. return (x, y, z)
'''

# Maps
print('''\nMaps:
map(function, sequence) calls function(item) for each item in
sequence and returns a list of the return values.''')

def cube(x): return x**3
print(map(cube, range(1,11)))

# Filters
print('''\nFilters:
filter(function, sequence) returns a list of items in sequence
for which function(item) is True
''')
def f(x):
    '''Divisible by 3 or 5'''
    return x % 3 == 0 or x % 5 == 0
print(filter(f, range(2, 25)))

# ----------------------------------------------
# Dictionaries
# ----------------------------------------------

heading('Dictionaries')

print('''
Dictionaries are a data structure indexed by keys, rather than
integers (as lists and strings are indexed).
A dictionary is an unordered set of key:value pairs, enclosed
within { }, with the requirement that keys are unique within a
given dictionary.
''')

# Assigning a dictionary
# --- Assign a list of key:value pairs
greek = { 'a': 'alpha', 'b': 'beta', 'g': 'gamma'}
print(greek['a'])
greek['d'] = 'delta' # Add a key:value pair
print(greek) # Prints keys
print(greek.keys()) # Same as above
#-- Or start with an empty dictionary, then add key:value pairs
suitcase = {}
suitcase['shirts'] = 5
suitcase['pants'] = 3

# Membership testing
print('a' in greek) # True
if 'z' in greek: print greek['z'] # No 'z' key so doesn't print
print(greek.get('z')) # None

# Looping over keys in a dictionary
# --- Two equivalent methods:
for key in greek: print key
for key in greek.keys(): print key

# Dictionary operations
inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone','dagger','bedroll','bread loaf'],
    'pocket': ['seashell', 'strange berry', 'lint']
}
print(inventory)
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pouch'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
for key in sorted(inventory.keys()):
    print('%s: %s' %(key, inventory[key]))


# ----------------------------------------------
# Modules, namespaces and scripts
# ----------------------------------------------

heading('Modules, namespaces and scripts')

print('''\
Modules:
- A python module is a .py file containing definitions and executable
  statements
- A triple-quoted comment at the beginning of the .py file is the
  documentation string for the module
- When importing other modules in a .py file, it is convention (although
  not required) to put all the import statements at the start of the file

Namespaces:
- A Python namespace is a variable name-to-object binding
- The ipython interactive shell contains a global namespace similar
  to a Matlab workspace
- Modules and functions define their own local namespaces

If you have source code in a .py file, e.g. zoo.py, you can use the
module in several ways:

1) Run as a script from the system shell command line:

python zoo.py

2) Run as a script within an ipython interactive session:

%run zoo.py
--> This runs the script in an empty namespace and loads all the results
    (variables, functions, etc.) into the global namespace of the
    interactive ipython shell.  The command %run is an ipython magic command
    that runs a Python script (see magic commands in later section).

%run zoo.py -i
--> Gives the script access to variables already defined in the interactive
    namespace

3) Import the module into an ipython interactive session:

import zoo
--> This runs all the code in zoo.py and stores its variables, functions,
    and classes in an object called 'zoo'.
''')

'''
More on modules
---------------

Suppose I have a module named zoo.py containing the following:

------- zoo.py -----------------------------------------
def visit(animals, name):
    print('Welcome to the zoo, ' + name + '! We have: ')
    for key in animals:
        print('  %d %s' % (animals[key], key))

animals = {'zebras': 5, 'elephants': 4, 'penguins': 10}
name = 'Jennifer'
visit(animals, name)
---------------------------------------------------------
'''
# Within an ipython interactive session:

# Import the module
import zoo

# I can use fully qualified variable and function names:
print(zoo.animals)
myanimals = {'tigers':2, 'koalas': 5}
zoo.visit(myanimals, 'Ivy')

# I can assign the visit function from zoo to a variable:
myvisit = zoo.visit
myvisit(myanimals, 'Jackson')

# Other options for importing:
import zoo as myzoo # Rename the module object
from zoo import visit # Import only the visit function from zoo

'''
Now suppose I edited zoo.py to add the opening hours to the end of the
greeting message in the visit function:
print('Our opening hours are Mon-Sun 8:00am - 8:00pm')

If I run zoo.py as a script in ipython, all the changes will be
implemented and the opening hours will be printed.

But if I have imported zoo.py as a module, the edits to the source file
will not be implemented in my ipython session.  If I try importing again
with 'import zoo', this just returns a reference to the previously loaded
module and the changes are still not propagated through.

To propagate changes in a module, run the command:
reload(zoo)

However, any dependencies (modules imported in zoo.py and their nested imports)
do not reload!  The command dreload(zoo) attempts a deep reload of all
dependencies, but doesn't always work.  So if you have a lot of imports
nested in modules, in order to propagate through source code edits you can
a) Exit ipython and start a new session, or
b) Use the %reset magic command to clear the ipython interactive namespace

If a script expects command line arguments, these can be passed to the script
after the file path in the %run command as though on the command line:
%run myscript.py 10

To access command line arguments, import the sys module with import sys and
use sys.argv.

For a list of all the objects defined in the current ipython namespace,
use the command:
dir()
'''

# ----------------------------------------------
# Text file I/O
# ----------------------------------------------

heading('Text file I/O')

# ----------------------------------------------------------------------
# Reading a file

filename = 'softkitty.txt'

# The special mode 'rU' is the "Universal" option for text files where it's
# smart about converting different line-endings so they always come through
# as a simple '\n'.
f = open(filename, 'rU')

# Iterate over the lines of the file
count = 0
for line in f:
    print(str(count) + ' ' + line)
    count += 1

# Close file
f.close()

# You can also read the entire contents of a file all at once into one
# giant string using .read()
f = open(filename, 'rU')
contents = f.read()
f.close()
print(contents)

# ----------------------------------------------------------------------
# Writing a file

outfile = 'out.txt'
f2 = open(outfile, 'w')
f2.write('Curiously enough, the only thing that went through the mind of\n')
f2.write('the bowl of petunias as it fell was "Oh no, not again". Many people\n')
f2.write('have speculated that if we knew exactly why the bowl of petunias\n')
f2.write('had thought that we would know a lot more about the nature of the\n')
f2.write('Universe than we do now.')
f2.close()

# -----------------------------------------------
# Handy modules
# ----------------------------------------------

heading('Handy modules')

# Date and time
print('Date and time')
from datetime import datetime

now = datetime.now()
now = ('%d/%d/%d %d:%d:%d' %
       (now.month, now.day, now.year, now.hour, now.minute, now.second))
print(now)

# ----------------------------------------------------------------------
# Random numbers
print('Random numbers')
import random

# Random decimal number in the interval [0, 1) (including 0, excluding 1)
x1 = random.random()
print(x1)

# Random integer in the range [a,b], including both end points
num = random.randint(1, 6)
print(num)

# ----------------------------------------------
# Sorting
# ----------------------------------------------

heading('Sorting')

# Sort a dictionary by key
myzoo = {'lions': 5, 'tigers': 3, 'bears': 4, 'penguins': 10}
for w in sorted(myzoo):
    print(str(w) + ' ' + str(myzoo[w]))

# Sort a dictionary by value, highest to lowest
sortlist = sorted(myzoo, key = myzoo.get, reverse=True)
for w in sortlist:
    print(str(w) + ' ' + str(myzoo[w]))

# ----------------------------------------------
# IPython features
# ----------------------------------------------

heading('IPython features')

print('''\
Keyboard shortcuts
------------------
Up/Down keys --> Back/forward in command history
Ctrl-a --> Move cursor to beginning of line
Ctrl-e --> Move cursor to end of line
Ctrl-u --> Discard all text on current line
Ctrl-k --> Discard all text after cursor on current line

Wildcards
---------
zoo.*anim*? --> Lists all names in module zoo containing 'anim'

Magic commands
--------------
These are command line programs that can be run within the ipython
shell.  They can be used without the % if no variable of the same name
has been defined.

%paste -->  Paste and run code from clipboard
%cpaste --> Paste code from clipboard (can then add more code or press
            enter to run)
%bookmark --> Bookmark a folder
%reset -->  Clears interactive namespace (like clear in Matlab)
!cmd -->    Runs a Unix system command in the ipython shell
            e.g. !head -n 10 myfile.txt

Use $foo to pass the value of ipython variable foo as an argument to a
command line magic command, e.g.:
foo = 'test*'
!ls $foo

Unassigned command outputs
--------------------------
_ gives last output
__ gives second last output


Logging
-------
To start or stop logging commands from the ipython session to a log file,
use the commands: logstart, logstop, logstate

Integration with matplotlib
---------------------------
Launch ipython with the --pylab option (i.e. ipython --pylab from command
line).  This allows plot windows to work properly and imports most of
the numpy and matplotlib modules into the interactive global namespace.

Notebooks
---------
From command line, launch ipython with:
ipython notebook
''')

# ----------------------------------------------
# Editor configuration
# ----------------------------------------------

heading('Editor configuration')

print('''\
My preferred text editor configuration (e.g. with Atom editor):
- Syntax highlighting
- Parentheses matching
- Tab = 4 spaces (make sure no actual Tab characters are used!)
- Auto-indent on
''')

# ----------------------------------------------
# Conventions and best practices
# ----------------------------------------------

heading('Conventions and best practices')

'''Note: some of these are not followed in this .py file because its
purpose is to mimic an interactive ipython session and easily copy/paste code
snippets.'''

print('''
Follow PEP 0008 -- Style Guide for Python, from the Python Developer's Guide
for consistent, readable code.
''')

'''
Naming Conventions
- CamelCase for classes
- lower_case_with_underscores for everything else
- Avoid built-in names such as str, len, list

Best Practices:
- Import statements at start of .py file
- Single line comments on their own line
- Maximum line width of 80 characters (for readability without text wrapping)
- First line of docstring is a concise summary of the function.  If including
  additional lines, separate them from the first line with a blank second line.
- Maintain larger modules, each with high internal cohesion, rather than many
  tiny separate files.  Aim for a sensible and intuitive module and package
  structure for a large codebase.
'''

# Zen of Python
# PEP 20 by Tim Peters, from the Python Developer's Guide
# https://www.python.org/dev/peps/pep-0020/
# Displays on the python console with the command 'import this'
print('''\
The Zen of Python

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
''')
