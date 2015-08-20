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

# Arrays of zeros, ones, and empty
zeros1 = np.zeros(10)
zeros2 = np.zeros((3, 6))
empty1 = np.empty((2, 3, 2)) # Empty arrays are initialized with misc garbage
ones1 = np.ones((4, 5))

# Ranges of numbers and evenly spaced line segements
x1 = np.arange(3, 15, 2) # ndarray version of Python built-in range() function
x2 = np.linspace(0, 4.5, 10) # Divides the range (inclusive) into 10 segments
# ----------------------------------------------------------------------
# Mathematical operations

# Basic math operations between arrays (or between an array and a scalar)
# are applied element-wise on the arrays
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
print(arr + 10)
print(arr * arr)
print(arr - arr)
print(1 / arr)
print(arr ** 0.5)

# Universal functions:  fast element-wise array functions
x1 = np.random.randn(5)
x2 = x1.round(2) # Round each element to 2 decimal places
print(x1)
print(x2)
arr = np.array([1., 4., 6., 9.])
print(np.sqrt(arr))
print(np.exp(arr))
x, y = np.random.randn(8).round(1), np.random.randn(8).round(1)
print(x)
print(y)
print(np.maximum(x, y)) # element-wise maximum
arr = (np.random.randn(7) * 5).round(2)
print(np.modf(arr)) # decimal and integer components of each element

# ----------------------------------------------------------------------
# Type conversions

# The astype() method of ndarray casts from one type to another
# -- Note: standard Python float corresponds to np.float64
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

# 1-D array
arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
arr[5:8] = 12
print(arr)

# 2-D array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])
print(arr2d[0][2])
print(arr2d[0, 2])

# 3-D array
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])
print(arr3d[1, 0])
old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
arr3d[0] = old_values
print(arr3d)

# ----------------------------------------------------------------------
# Slices - views vs. copies

print('''\
Array slices are *views* on the original array, not copies, so if you modify
a view, the source array is modified too! To copy a slice, use .copy()
''')
arr = np.arange(10)
print(arr)
slice1 = arr[2:7] # slice1 is a view on arr
print(slice1)
slice1[:2] = -42 # This modifies the source array 'arr' also!
print(slice1)
print(arr) # Has changed!

# To make a copy of a slice, rather than a view, use the .copy() method
arr = np.arange(10)
print(arr)
slice1 = arr[2:7].copy() # Now we have a copy of the contents
print(slice1)
slice1[:2] = -42 # arr does not change
print(slice1)
print(arr) # The same as before!

# ----------------------------------------------------------------------
# Boolean indexing

cats = np.array(['tabby', 'calico', 'siamese', 'tabby', 'siamese',
    'calico', 'calico'])

def numbers_array(nrow, ncol):
    return np.arange(nrow*ncol).reshape((nrow, ncol))

data = numbers_array(7, 4)
data[:,2] -= 20
print(cats)
print(data)

print(cats == 'tabby')
print(data[cats == 'tabby'])
print(data[cats == 'tabby', 2:])
print(data[cats == 'tabby', 3])

# numpy uses &, | and ! instead of and, or and not as in built-in Python
print(data[cats != 'tabby'])
print(data[-(cats == 'tabby')]) # Same as data[cats != 'tabby']
mask = (cats == 'tabby') | (cats == 'siamese')
print(mask)
print(data[mask])

# Change parts of the ndarray selected by Boolean indexing
data[data < 0] = 0
print(data)
data[cats != 'calico'] = -5
print(data)

# Note: Unlike slicing with numeric indices, Boolean indexing always creates
# a copy of the data.
subset = data[cats == 'calico'] # Makes a copy
print(subset)
subset[0] = 10 # Changes subset but not data
print(subset)
print(data) # Same as before

# ----------------------------------------------------------------------
# Fancy indexing

a = numbers_array(8, 4)
print(a)
print(a[[4, 0, 2]]) # Rows 4, 0, 2
print(a[[-1, -3]]) # Rows -1 (last) and -3 (3rd last)
print(a[[1, 5, 7, 2], [0, 3, 1, 2]]) # Elements [1,0], [5,3], [7,1], [2,2]
print(a[[1, 5, 7, 2]][:, [0, 2]]) # Columns 0 and 2 of rows 1, 5, 7, 2

# The np.ix_ function returns an open mesh from multiple sequences
print(a[np.ix_([1,3], [2,0])]) # [[a[1,2] a[1,0]], [a[3,2] a[3,0]]]

# ----------------------------------------------------------------------
# Expressing conditional logic as array operations

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(result)
result = np.where(cond, xarr, yarr) # Vectorized version of above
print(result)

arr = np.random.randn(4, 4).round(1)
print(arr)
print(np.where(arr > 0, 2, -2))
print(np.where(arr > 0, 2, arr)) # set only positive values to 2

# ----------------------------------------------------------------------
# Transposing arrays and swapping axes

arr = numbers_array(3, 5)
print(arr)
print(arr.T) # Transpose

arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print(arr.transpose((1, 0, 2)))
print(arr.swapaxes(1, 2))

# ----------------------------------------------------------------------
# Linear algebra

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x.dot(y))  # Dot product using .dot() method
print(np.dot(x,y)) # Dot product using np.dot()

X = np.random.randn(5, 5).round(1)
mat = X.T.dot(X)
inv = np.linalg.inv(mat)
print(mat.round(2))
print(inv.round(2))
print(mat.dot(inv).round(2))

# ----------------------------------------------------------------------
# Mathematical and statistical methods

arr = np.random.randn(5, 4).round(2)
print(arr.mean())
print(np.mean(arr)) # Equivalent to .mean()
print(arr.mean(axis=0)) # Specify which axis to operate along

print(arr.sum())
print(arr.sum(axis=1)) # Sum along axis 1
print(arr.sum(1)) # Equivalent to .sum(1)

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr.cumsum(0)) # Cumulative sum along axis 0
print(arr.cumprod(1)) # Cumulative product along axis 1

# Methods for boolean arrays
arr = np.random.randn(100)
npos = (arr > 0).sum() # Number of positive values in arr

bools = np.array([False, False, True, False])
bools.any() # True if any element in bools is True
bools.all() # True if all elements in bools are True

# ----------------------------------------------------------------------
# Sorting

arr = np.random.randn(8).round(1)
print(arr)
arr.sort() # Sorts the array in place
print(arr)

arr = np.random.randn(5, 3).round(1)
print(arr)
arr.sort(1) # Sort along axis 1
print(arr)

large_arr = np.random.randn(1000)
large_arr.sort()
quant5 = large_arr[int(0.05 * len(large_arr))] # 5% quantile
print(quant5)

# ----------------------------------------------------------------------
# Unique and other set logic

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names)) # ndarray of unique names
print(set(names)) # Python set object of unique names
print(sorted(np.unique(names))) # Sorted ndarray
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))

values = np.array([6, 0, 0, 3, 2, 5, 6])
in_val = np.in1d(values, [2, 3, 6]) # in_val[i]=True if values[i] is 2, 3 or 6

# ----------------------------------------------------------------------
# File input and output with arrays

# Storing arrays on disk in binary format
arr = np.arange(10)
np.save('some_array', arr)
np.load('some_array.npy')

# Loading text files
'''
arr = np.loadtxt('array_ex.txt', delimiter=',')
'''


# ----------------------------------------------------------------------
# matplotlib
# ----------------------------------------------------------------------

heading('matplotlib:  2-D plots and visualizations')

print('''\
When running a script in ipython, the figures usually aren't visible when
the script completes.  To show them:
plt.show()

To close figure windows:
plt.close(1)        # Closes figure 1
plt.close('all')    # Closes all open figure windows
''')

points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
plt.pcolormesh(xs, ys, z, cmap=plt.cm.gray)
plt.colorbar()
plt.title('$\sqrt{x^2 + y^2}$ for a grid of values')

# Create a new figure with jet colormap
plt.figure()
plt.pcolormesh(xs, ys, z, cmap=plt.cm.jet)
plt.colorbar()

# ----------------------------------------------------------------------
# Example from matplotlib tutorial at
# http://www.labri.fr/perso/nrougier/teaching/matplotlib/
# Line plot with default formatting and customized formatting
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# Default formatting
plt.figure()
plt.plot(X,C)
plt.plot(X,S)

# Customized formatting
plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-",  label="sine")

plt.xlim(X.min()*1.1, X.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.ylim(C.min()*1.1,C.max()*1.1)
plt.yticks([-1, +1],
           [r'$-1$', r'$+1$'])

plt.legend(loc='upper left', frameon=False)

t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)],
         color ='blue',  linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)),  xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)],
         color ='red',  linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)),  xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))


# ----------------------------------------------------------------------
# basemap
# ----------------------------------------------------------------------

heading('basemap: Plotting geographic data')

# Super duper easy first map
# Default projection is 'cyl' (Cylindrical Equidistant projection)
plt.figure()
m = Basemap()
m.drawcoastlines()
m.drawcountries()

# Use 'ortho' projection to make a fancy globe with shaded continents
plt.figure()
m = Basemap(projection='ortho', lat_0=0, lon_0=0)
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',lake_color='aqua')
m.drawcoastlines()

# Plot a point on the map
plt.figure()
m = Basemap(projection='cyl')
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',lake_color='aqua')
m.drawcoastlines()
# Add a point at 30W, 20 N using m.plot()
x, y = m(-30, 20)
m.plot(x, y, marker='*', color='m')
# Add a bunch of points using m.scatter()
lons = [0, 10, -20, -20]
lats = [0, -10, 40, -20]
x, y = m(lons, lats)
m.scatter(x, y, marker='D',color='r')


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
