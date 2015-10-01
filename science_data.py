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

with xray.open_dataset(filename) as ds:
    # xray.open_dataset() does a lazy load of the file
    # To fully load the contents into memory and make the dataset available
    # after the file is closed, use the .load() method:
    ds.load()

print(ds)

# Unpack some data from xray object into numpy arrays
lat = ds['lat'].values
lon = ds['lon'].values
lev = ds['lev'].values
ps = ds['ps'].values/100 # Convert Pa to hPa
xi, yi = np.meshgrid(lon, lat)

# Plot on basemap
plt.figure()
m = Basemap()
m.drawcoastlines()
m.pcolormesh(xi, yi, ps, cmap='jet', latlon=True)
m.colorbar()
plt.draw()

# Let's put this all in a function to show how xray DataArrays
# make life easier
def plotmap(data, cmap='jet', latname='lat', lonname='lon'):
    lat, lon = ds[latname], ds[lonname]
    xi, yi = np.meshgrid(lon, lat)

    # Plot on basemap
    plt.figure()
    m = Basemap()
    m.drawcoastlines()
    m.pcolormesh(xi, yi, data, cmap=cmap, latlon=True)
    m.colorbar()
    plt.draw()

# We can extract one vertical level from all the variables in the
# dataset with one command:
k = 2 # 850 mb
ds850 = ds.isel(lev=k)
print(ds850)

# We can work with a bunch of data variables without needing
# separate variables to store all their coordinates.  In this simple
# example the variables below all have the same grid, so it doesn't
# really matter, but this feature comes in very handy when you have
# multiple datasets or output from models at different resolutions.
u = ds850['u']
v = ds850['v']
T = ds850['T']
plotmap(u, cmap='RdBu_r')
plotmap(v, cmap='RdBu_r')
plotmap(T)

# Calculate the mean along a named dimension (don't need to know which
# axis it is in the array)
ubar = u.mean(dim='lon')
plt.figure()
plt.plot(ubar.lat, ubar)

# ----------------------------------------------------------------------
# Create a new dataset and save to netcdf file

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
