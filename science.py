'''
Jennifer's cheat sheet for scientific computing with Python.
- numpy:        Numerical python for N-D arrays, linear algebra, etc
- matplotlib:   2-D plots and visualizations
- basemap:      Plotting geographic data
- pandas:       Statistics for tabular (spreadsheet-like data)
- xray:         N-D labeled datasets and netCDF I/O

Each section of this cheatsheet can be copy/pasted into ipython (using the
%paste magic command for indented code) and run separately in an interactive
session.

Many of these code snippets are pilfered / adapted from:
- Python for Data Analysis by Wes McKinney
  https://github.com/pydata/pydata-book
- Matplotlib tutorial
  http://www.labri.fr/perso/nrougier/teaching/matplotlib/
- Basemap tutorial
  https://basemaptutorial.readthedocs.org/en/latest/index.html
- Xray user guide http://xray.readthedocs.org/en/stable/index.html
'''

# Naming conventions for importing standard scientific modules:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Additional modules useful for atmospheric science
from mpl_toolkits.basemap import Basemap
import xray

# ----------------------------------------------------------------------
print("\nWelcome to Jennifer's cheat sheet for scientific computing in Python!")

def heading(s):
    '''Prints a nice heading to the console.'''
    line = '-' *60
    print('\n' + line + '\n' + s + '\n' + line)

# ----------------------------------------------------------------------
# numpy
# ----------------------------------------------------------------------

heading('numpy: N-D arrays, linear algebra, FFT, random numbers\n'
    'and other numerical operations.')

# ----------------------------------------------------------------------
# ndarray basics

print('''
An N-D array in numpy is an object of type ndarray, a multi-dimensional
container for homogeneous data (i.e. all elements must be the same type).
''')

# Generate a 2x3 ndarray of random numbers
data = np.random.randn(2, 3)
print(data)

# The ndarray object attributes include the data type, dimension and shape
print(data.dtype)
print(data.ndim)
print(data.shape)

# Create ndarrays from Python lists
# -- If the data type isn't specified, numpy makes a smart guess based
#    on the contents of the array
list1 = [6, 7.5, 8, 0, 1]   # Python list
data1 = np.array(list1) # Numpy 1-D array
print(data1)
print(data1.dtype)

list2 = [[1, 2, 3, 4], [5, 6, 7, 8]] # Python nested list
data2 = np.array(list2) # Numpy 2-D array
print(data2)
print(data2.dtype)
print(data2.ndim)
print(data2.shape)

# Specifying data types for ndarrays
data1 = np.array([1, 2, 3], dtype=np.float64)
data2 = np.array([1, 2, 3], dtype=np.int32)
print(data1.dtype)
print(data2.dtype)

# Arrays of zeros, ones, empty, and ranges
zeros1 = np.zeros(10)
zeros2 = np.zeros((3, 6))
empty1 = np.empty((2, 3, 2)) # Empty arrays are initialized with misc garbage
ones1 = np.ones((4, 5))
x1 = np.arange(15) # ndarray version of Python built-in range() function

# ----------------------------------------------------------------------
# Mathematical operations

# Basic math operations between arrays (or between an array and a scalar)
# operate element-wise on the arrays
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
print(arr + 10)
print(arr * arr)
print(arr - arr)
print(1 / arr)
print(arr ** 0.5)

# ----------------------------------------------------------------------
# Type conversions

# The astype() method of ndarray casts from one type to another
arr = np.array([1, 2, 3, 4, 5])
float_arr = arr.astype(np.float64)
print(arr.dtype, float_arr.dtype)

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
int_arr = arr.astype(np.int32)
print(arr)
print(int_arr)

# Converting numeric strings to numbers
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
arr = numeric_strings.astype(np.float64)

# Converting to the same dtype as another variable
int_array = np.arange(10)
float_array = np.array([1.0, 2.5, -3.1], dtype=np.float64)
arr = int_array.astype(float_array.dtype)

# ----------------------------------------------------------------------
# Basic indexing and slicing


# ----------------------------------------------------------------------
# matplotlib
# ----------------------------------------------------------------------

heading('matplotlib:  2-D plots and visualizations')


# ----------------------------------------------------------------------
# basemap
# ----------------------------------------------------------------------

heading('basemap: Plotting geographic data')

m = Basemap()
m.drawcoastlines()
m.drawcountries()

# ----------------------------------------------------------------------
# pandas
# ----------------------------------------------------------------------

heading('pandas:  Statistics for tabular (spreadsheet-like) data')


# ----------------------------------------------------------------------
# xray
# ----------------------------------------------------------------------

heading('xray:  N-D labeled datasets and netCDF I/O')


filename = 'data/MERRA.201401.SUB.nc'
dataset = xray.open_dataset(filename)
