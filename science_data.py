'''
Jennifer's cheat sheet for scientific computing with Python - data analysis
with xray and pandas.

Each section of this cheatsheet can be copy/pasted into ipython (using the
%paste magic command for indented code) and run separately in an interactive
session.

Many of these code snippets are pilfered / adapted from:-
- Xray user guide http://xray.readthedocs.org/en/stable/index.html

This cheatsheet is part of a set: science_numpy.py, science_plots.py, and
science_data.py, covering the following scientific computing modules, with
a focus on atmospheric science applications:
- numpy:        Numerical python for N-D arrays, linear algebra, etc
- matplotlib:   2-D plots and visualizations
- basemap:      Plotting geographic data
- pandas:       Statistics for tabular (spreadsheet-like data)
- xray:         N-D labeled datasets and netCDF I/O
'''

# Naming conventions for importing standard scientific modules:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Additional modules useful for atmospheric science
from mpl_toolkits.basemap import Basemap
import xray

# ----------------------------------------------------------------------
print("\nWelcome to Jennifer's cheatsheet for scientific computing in Python!")

def heading(s):
    '''Prints a nice heading to the console.'''
    line = '-' *60
    print('\n' + line + '\n' + s + '\n' + line)

heading('Data analysis with xray and pandas')
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# pandas
# ----------------------------------------------------------------------

heading('pandas:  Statistics for tabular (spreadsheet-like) data')


# ----------------------------------------------------------------------
# xray
# ----------------------------------------------------------------------

heading('xray:  N-D labeled datasets and netCDF I/O')


#filename = 'data/MERRA.201401.SUB.nc'
filename = 'data/eraI_1979_monthly.nc'
dataset = xray.open_dataset(filename)

# Unpack from xray object into numpy arrays
lat = dataset['latitude'].values
lon = dataset['longitude'].values
level = dataset['level'].values
u = dataset['u'].values
v = dataset['v'].values
temp = dataset['t'].values

xi, yi = np.meshgrid(lon, lat)

m, k = 1, -4 # Month 1, level 850 mb

u1 = u[m, k, :, :]

plt.figure()
plt.pcolormesh(xi, yi, u1, cmap='jet')
plt.colorbar()
plt.axis([0, 360, -90, 90])

plt.figure()
m = Basemap()
m.drawcoastlines()
cmesh = m.pcolormesh(xi, yi, u1, cmap='jet', latlon=True)
cb = m.colorbar(cmesh, location='right', size='5%', pad='2%')
plt.draw() # Need this to make the colorbar visible
