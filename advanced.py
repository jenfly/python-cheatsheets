"""
Jennifer's cheatsheet for advanced Python topics.

Contents:
- Classes
- Collections module
- Argument unpacking
- Errors and exceptions
- Fancier file I/O
- sys module

Each section of this cheatsheet can be copy/pasted into ipython (using
the %paste magic command for indented code) and run separately in an
interactive session.

Many of these code snippets are pilfered / adapted from:
- https://docs.python.org/2/tutorial/
- http://www.tutorialspoint.com/python/python_classes_objects.htm
"""

# Make float division the default for / operator, even when the
# operands are both integers
from __future__ import division

import math
import collections
import nltk

print("\nWelcome to Jennifer's advanced Python cheatsheet!")

def heading(s):
    """Print a nice heading to the console."""
    line = '-' * 40
    print('\n' + line + '\n' + s + '\n' + line)

# ----------------------------------------------------------------------
# Classes
# ----------------------------------------------------------------------

heading('Classes')

# Defining a class
class Vector:
    """Vector in x,y plane."""

    def __init__(self, x, y):
        """Initialize instance object with a call like v = Vector(x, y)."""
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        """Return a printable string representation of the instance object."""
        return 'Vector (%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        """Overload the + operator to perform vector addition."""
        return Vector(self.x + other.x, self.y + other.y)

    def length(self):
        """Return the length of the vector measured from the origin."""
        return math.sqrt(self.x**2 + self.y**2)

    def angle(self, degrees=True):
        """
        Return the angle of the vector from the x-axis.

        Default units are degrees. If argument degrees=False, return the
        angle in radians.
        """
        theta = math.atan(self.y / self.x)
        if self.x < 0:
            theta += math.pi
        if degrees:
            theta = math.degrees(theta)
        return theta

    def distance(self, other):
        """Return the distance between the endpoints of two vectors."""
        return math.sqrt( (other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def disp(self):
        """Print detailed information about the vector."""
        print(self)
        print('  Length: %f' % self.length())
        print('  Angle: %f degrees' % self.angle())


# Using the class
v1 = Vector(2, 10)
print(v1)

# Calling v1.length() is equivalent to Vector.length(v1)
print(v1.length())
print(v1.angle(degrees=False))
v1.disp()

v2 = Vector(-5, 2)
print(v1 + v2)
print(v1.distance(v2))

# Making a standalone function with vector objects as input
def vdistance(v1, v2):
    """Return distance between endpoints of two Vector objects.)"""
    return math.sqrt( (v2.x - v1.x) ** 2 + (v2.y - v1.y) ** 2)

# vdistance(v1, v2) is now equivalent to v1.distance(v2)
print(vdistance(v1, v2))


# ----------------------------------------------------------------------
# Collections module
# ----------------------------------------------------------------------

filename = 'data/softkitty.txt'

with open(filename, 'rU') as f:
    contents = f.read()

# Split into a list of words using the natural language toolkit
# This splits out punctuation, which contents.split() does not do.
contents = nltk.word_tokenize(contents)

# If nltk is not installed, then use:
# contents = contents.split()

# A defaultdict from the collections module creates a dict where a new key:value
# pair is initialized with a default value when assigning to a key that
# doesn't exist
word_counts = collections.defaultdict(int)

for word in contents:
    word_counts[word] += 1

# A Counter object from the collections module creates a dict with the keys
# as the unique elements in a list, and the values the number of times the
# element occurs in the list
word_counts2 = collections.Counter(contents)
print(word_counts2)
print('Most common:')
for word, count in word_counts2.most_common(5):
    print(word, count)


# ----------------------------------------------------------------------
# Argument unpacking
# ----------------------------------------------------------------------

def magic(*args, **kwargs):
    # args is a tuple of unnamed arguments.
    # kwargs is a dict of named arguments
    print('Unnamed args', args)
    print('Keyword args', kwargs)

magic(1, 2, key='word', key2='word2')

def other_way_magic(x, y, z):
    print('x', x)
    print('y', y)
    print('z', z)
    return x + y + z

x_y_list = [1, 2]
z_dict = {'z' : 3}
print(other_way_magic(*x_y_list, **z_dict))

# ----------------------------------------------------------------------
# Fancier file I/O
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Errors and exceptions
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# sys module
# ----------------------------------------------------------------------
