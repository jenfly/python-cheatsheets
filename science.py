'''
- numpy
- pandas
- matplotlib
- scipy
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import xray

#from netCDF4 import Dataset
#import scipy.io.netcdf as nc

filename = 'data/MERRA.201401.SUB.nc'
dataset = xray.open_dataset(filename)


'''
f = nc.netcdf_file(filename, 'r')
print(f.variables)
lat = np.copy(f.variables['latitude'])
lon = np.copy(f.variables['longitude'])
ps = f.variables['ps']
temp = f.variables['t']
time = f.variables['time']
f.close()
'''

'''
fh = Dataset(filename, mode='r')
lon = np.copy(fh.variables['longitude'])
lat = np.copy(fh.variables['latitude'])
ps = np.copy(fh.variables['ps'])
print(lon.shape)
print(lat.shape)
print(ps.shape)
fh.close()
'''



m = Basemap()
m.drawcoastlines()
m.drawcountries()
