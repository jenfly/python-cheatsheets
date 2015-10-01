"""
Jennifer's scientific computing cheatsheet - data analysis with xray and pandas.

Each section of this cheatsheet can be copy/pasted into ipython (using
the %paste magic command for indented code) and run separately in an
interactive session.

Many of these code snippets are pilfered / adapted from:-
- xray user guide http://xray.readthedocs.org/en/stable/index.html

This cheatsheet is part of a set: science_numpy.py, science_plots.py,
science_prettyplots, and science_data.py, covering the following
scientific computing modules, with a focus on atmospheric science
applications:
- numpy:        Numerical python for N-D arrays, linear algebra, etc
- matplotlib:   2-D plots and visualizations
- basemap:      Plotting geographic data
- pandas:       Statistics for tabular (spreadsheet-like data)
- xray:         N-D labeled datasets and netCDF I/O
"""

# Make float division the default for / operator, even when the
# operands are both integers
from __future__ import division

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
    """Print a nice heading to the console."""
    line = '-' *60
    print('\n' + line + '\n' + s + '\n' + line)

heading('Data analysis with xray and pandas')
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Overview
# ----------------------------------------------------------------------

heading('Overview')

print("""
Broad categories of data analysis tasks in Python
(Python for Data Analysis, by Wes McKinney)

- Interaction:      Interacting with outside world (file I/O)
- Preparation:      Cleaning, munging, combining, normalizing, reshaping,
                    slicing and dicing
- Transformation:   Applying math and statistics operations to datasets
                    or groups of datasets to derive new datasets
                    (e.g. aggregating)
- Modeling & computation:   Connecting your data to statistical models,
                    machine learning algorithms, or other computational tools
- Presentation:     Creating static or interactive graphical visualizations or
                    textual summaries

Terminology:
Munge / munging / wrangling:  The process of manipulating unstructured and/or
messy data into a structured or clean form.
""")


# ----------------------------------------------------------------------
# pandas
# ----------------------------------------------------------------------

heading('pandas:  Statistics for tabular (spreadsheet-like) data')

print('Coming soon!')

# ----------------------------------------------------------------------
# xray
# ----------------------------------------------------------------------

heading('xray:  N-D labeled datasets and netCDF I/O')

# ----------------------------------------------------------------------
# Reading data from a netcdf file

filename = 'data/ncep2_climatology_ann.nc'

# Open a netCDF file
ds = xray.open_dataset(filename) 

# ds is an xray.Dataset object containing all the variables and metadata
# from the netCDF file
print(ds)

# List of data variables in the dataset:
print(ds.data_vars)

# List of coordinates in the dataset:
print(ds.coords)

# List of dataset attributes:
print(ds.attrs)

# Get one of the data variables:
ps = ds['ps'] 

# ps is an xray.DataArray object, including coordinates and other metadata:
print(ps)
print('Coordinates:')
print(ps.coords)
print('Dimensions:')
print(ps.dims)
print('Attributes:')
print(ps.attrs)

# Close the file when done with it
ds.close() 

# The command ds = xray.open_dataset() does a lazy load of the file, so data 
# is loaded into memory only as needed and is only available as long as the 
# file is open.

# After ds.close(), we can no longer access the contents of ds or ps
# If we wanted our variable ps to be available after the file is closed,
# we would use ps = ds['ps'].load() to load it into memory.

# To make sure that files get properly closed out even if there is an error,
# it's better to use a context manager `with ... as :`
with xray.open_dataset(filename) as ds:
    # Here we extract whatever data we need and use .load() if we want to use
    # it later outside of the context manager.
    # This is a small dataset so we'll load the entire contents into memory:
    ds.load()

print(ds)

# We can unpack data from an xray object into numpy arrays with .values:
lat = ds['lat'].values
lon = ds['lon'].values
lev = ds['lev'].values
ps_vals = ds['ps'].values

def plotmap(data, lat=None, lon=None, cmap='jet'):
    # If data is a DataArray, we can omit the lat, lon arrays and extract
    # from the DataArray's coordinates
    if isinstance(data, xray.DataArray):
        lat, lon = data['lat'], data['lon']

    xi, yi = np.meshgrid(lon, lat)
    plt.figure()
    m = Basemap()
    m.drawcoastlines()
    m.pcolormesh(xi, yi, data, cmap=cmap, latlon=True)
    m.colorbar()
    plt.draw()

# Plot the data from numpy arrays
plotmap(ps_vals/100, lat, lon)

# Plot the data from DataArray
plotmap(ds['ps']/100)

# With DataArrays, we can work with a bunch of data variables without needing
# separate variables to store all their coordinates.  In this simple example 
# the variables below all have the same grid, so it doesn't really matter, but 
# this feature comes in very handy when you have multiple datasets or output 
# from models at different resolutions.
u = ds['u']
v = ds['v']
T = ds['T']
k = 2       # 850 mb
print(u[k]) # DataArray with 850 mb data
plotmap(u[k], cmap='RdBu_r')
plotmap(v[k], cmap='RdBu_r')
plotmap(T[k])

# Calculate the mean along a named dimension (don't need to know which
# axis it is in the array)
ubar = u[k].mean(dim='lon')
plt.figure()
plt.plot(ubar.lat, ubar)

# We can also apply operations to all the data variables in a dataset with
# one command, and using named dimensions.
print('Zonal mean')
dsbar = ds.mean(dim='lon')
print(dsbar)
print('Boom!')
ubar2 = dsbar['u'][k]
plt.figure()
plt.plot(ubar2.lat, ubar2)

# ----------------------------------------------------------------------
# Create a new dataset object and save to netcdf file

ds2 = xray.Dataset()
ds2.attrs['title'] = 'My Dataset'
ds2.attrs['source'] = 'Grumpy Cat'
ds2['ps'] = (('lat', 'lon'), ps)
ds2.coords['lat'] = ('lat', lat)
ds2.coords['lon'] = ('lon', lon)
print(ds2)

# Save to netcdf
outfile = 'data/out.nc'
ds2.to_netcdf(outfile, mode='w')

# ----------------------------------------------------------------------
# Reading OPenDAP data files

remote_file = 'http://iridl.ldeo.columbia.edu/SOURCES/.OSU/.PRISM/.monthly/dods'

with xray.open_dataset(remote_file, decode_times=False) as remote_ds:
    print(remote_ds)
    # Load a subset of max temperature data
    Tmax = remote_ds['tmax'][0, ::3, ::3].load()

print(Tmax)
plt.figure(figsize=(9,5))
plt.gca().patch.set_color('0')
plt.contourf(Tmax['X'], Tmax['Y'], Tmax.values, 20, cmap='RdBu_r')
plt.colorbar(label='Tmax (deg C)')
