'''
- numpy
- pandas
- matplotlib
- scipy
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import netCDF4 as nc

filename = 'data/MERRA.201401.SUB.nc'
fh = Dataset(filename, mode='r')
lon = fh.variables['longitude'][:]
lat = fh.variables['latitude'][:]
ps = fh.variables['ps'][:]
print(lon.shape)
print(lat.shape)
print(ps.shape)
fh.close()

m = Basemap()
m.drawcoastlines()
m.drawcountries()
