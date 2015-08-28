"""
Jennifer's scientific computing cheatsheet - matplotlib and basemap.

Contents:
- matplotlib basics
- Subplots
- Histograms
- Annotations
- Bar charts
- Scatter plots
- Fill plots
- Logarithmic axes
- Reverse axis direction
- Heat maps and contour plots
- Quiver plots
- Basemap

This cheatsheet covers the basic commands to create plots.  See
science_prettyplots.py for fancy formatting commands.

Each section of this cheatsheet can be copy/pasted into ipython (using
the %paste magic command for indented code) and run separately in an
interactive session.


Many of these code snippets are pilfered / adapted from:
- Matplotlib documentation
  http://matplotlib.org/users/pyplot_tutorial.html
- Matplotlib tutorial
  http://www.labri.fr/perso/nrougier/teaching/matplotlib/
- Basemap tutorial
  https://basemaptutorial.readthedocs.org/en/latest/index.html

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

# Naming conventions for importing standard scientific modules:
import numpy as np
import matplotlib.pyplot as plt

# Additional modules useful for atmospheric science
from mpl_toolkits.basemap import Basemap
import xray

# ----------------------------------------------------------------------
print("\nWelcome to Jennifer's cheatsheet for scientific computing in Python!")

def heading(s):
    """Print a nice heading to the console."""
    line = '-' *60
    print('\n' + line + '\n' + s + '\n' + line)

heading('Plotting with matploblib and basemap')
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# matplotlib basics
# ----------------------------------------------------------------------

heading('matplotlib:  2-D plots and visualizations')

print("""\
When running a script in ipython, the figures usually aren't visible when
the script completes.  To show them:
plt.show()

Other operations with figure windows:
plt.figure()        # Creates a new figure window
plt.get_fignums()   # Returns a list of all the figures currently open
plt.draw()          # Refresh current figure (in case changes weren't applied)
plt.clf()           # Clears the current figure
plt.cla()           # Clears the current axes
plt.close(1)        # Closes figure 1
plt.close('all')    # Closes all open figure windows
plt.savefig('fig.eps') # Saves the figure in the current window to file
""")

# ----------------------------------------------------------------------
# Simple plot using format strings such as 'r-'
t = np.arange(0., 5., 0.2)

plt.figure()
plt.plot(t, t, 'r-', t, t**2, 'bs', t, t**3, 'g^')
plt.xlabel('t')
plt.ylabel('f(t)')

# ----------------------------------------------------------------------
# Using keyword arguments, formatting ticks, adding legends and labels

pi = np.pi
X = np.linspace(-pi, pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.figure()
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label='cosine')
plt.plot(X, S, color="red", linewidth=2.5, linestyle="--", label='sine')

# Specify ticks and tick labels
# -- the r'' in the tick label indicates that it is a raw string so that
#    Python doesn't treat the \ as an escape character (lets the LaTeX
#    interpreter take care of it)
plt.xticks([-pi, -pi/2, 0, pi/2, pi],
    [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.ylim(C.min()*1.1, C.max()*1.1)

# Add labels
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Line Plot')

# Add legend
# -- Uses the labels specified in the plot() commands
plt.legend(loc='upper left', frameon=False)

# ----------------------------------------------------------------------
# Subplots
# ----------------------------------------------------------------------

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.figure()
plt.subplot(2, 1, 1)    # plt.subplot(numrows, numcols, numfig)
plt.plot(x1, y1, 'yo-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

# The commas can be omitted in subplot() if numrows, numcols and numfig
# are all less than 10
plt.subplot(212)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

# To tighten up the space between and around subplots, use tight_layout()
plt.tight_layout()

# ----------------------------------------------------------------------
# Histogram
# ----------------------------------------------------------------------

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# Histogram of the data
plt.figure()
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')

# Add a text annotation
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')

# Set limits for both axes together: [xmin, xmax, ymin, ymax]
plt.axis([40, 160, 0, 0.03])

# Turn on grid lines
plt.grid(True)

# ----------------------------------------------------------------------
# Annotations
# ----------------------------------------------------------------------

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*pi*t)

plt.figure()

# Return handles to axes and line object
ax = plt.subplot(111)
line, = plt.plot(t, s, lw=2)
plt.ylim(-2,2)

# Annotate with arrow and text
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

# ----------------------------------------------------------------------
# Bar charts
# ----------------------------------------------------------------------

n_groups = 5
means_men = (20, 35, 30, 35, 27)
std_men = (2, 3, 4, 1, 2)
means_women = (25, 32, 34, 20, 25)
std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_men, bar_width, alpha=opacity,
            color='b', yerr=std_men, error_kw=error_config, label='Men')

rects2 = plt.bar(index + bar_width, means_women, bar_width, alpha=opacity,
            color='r', yerr=std_women, error_kw=error_config, label='Women')

plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))
plt.legend()
plt.tight_layout()

# ----------------------------------------------------------------------
# Scatter plots
# ----------------------------------------------------------------------

n = 1024
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
angle = np.arctan2(y,x)         # Angle from x-axis
dist = np.sqrt(x**2 + y**2)     # Distance from origin
dist = dist * 20                # Scaling for plotting purposes
axlim = [-3, 3, -3, 3]
fnt = {'fontsize': 11}

plt.figure(figsize=(7, 7))

# Simple scatter plot using plot()
# -- Points on the plot are all the same size and color
plt.subplot(2,2,1)
plt.plot(x, y, 'bo')
plt.title('plot()', fnt)
plt.axis(axlim)

# Same thing using scatter() without any additional arguments
plt.subplot(2,2,2)
plt.scatter(x, y)
plt.title('scatter()', fnt)
plt.axis(axlim)

# Use the scatter() function to have size and/or color vary by point
# -- Optional keyword arguments include:
#     s = marker size (scalar or array)
#     c = marker color (scalar or array)
#     marker = marker style
#     alpha = transparency (0-1)

# Scatter plot with marker size corresponding to distance from origin
plt.subplot(2,2,3)
plt.scatter(x, y, s=dist)
plt.title('s=dist', fnt)
plt.axis(axlim)

# Marker size scales as distance from origin, and marker color scales as
# angle from x-axis, with 50% transparency and jet colormap
plt.subplot(2,2,4)
plt.scatter(x, y, s=dist, c=angle, alpha=0.5, cmap='jet')
plt.title('s=dist, c=angle,\nalpha=0.5, cmap=jet', fnt)
plt.axis(axlim)

# ----------------------------------------------------------------------
# Fill plots
# ----------------------------------------------------------------------

x = np.linspace(0, 1, 1000)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

plt.figure()

# Fill between curve and x-axis using fill()
plt.subplot(2,1,1)
plt.fill(x, y, 'r')
plt.grid(True)

# Fill between specified values of y using fill_between()
plt.subplot(2,1,2)
plt.plot(x, y, 'k')
plt.fill_between(x, 0.2, y, y > 0.2,color='red', alpha=.25)
plt.fill_between(x, y, -0.1, y < -0.1, color='blue', alpha=.25)
plt.grid(True)

# ----------------------------------------------------------------------
# Logarithmic axes
# ----------------------------------------------------------------------
t = np.arange(0.01, 20.0, 0.01)

plt.figure()
plt.subplots_adjust(hspace=0.4)

# log y axis
plt.subplot(221)
plt.semilogy(t, np.exp(-t/5.0))
plt.title('semilogy')
plt.grid(True)

# log x axis
plt.subplot(222)
plt.semilogx(t, np.sin(2*np.pi*t))
plt.title('semilogx')
plt.grid(True)

# log x and y axis
plt.subplot(223)
plt.loglog(t, 20*np.exp(-t/10.0), basex=2)
plt.grid(True)
plt.title('loglog base 4 on x')

# with errorbars: clip non-positive values
ax = plt.subplot(224)
ax.set_xscale("log", nonposx='clip')
ax.set_yscale("log", nonposy='clip')

x = 10.0**np.linspace(0.0, 2.0, 20)
y = x**2.0
plt.errorbar(x, y, xerr=0.1*x, yerr=5.0+0.75*y)
ax.set_ylim(ymin=0.1)
ax.set_title('Errorbars go negative')

# ----------------------------------------------------------------------
# Reverse axis direction
# ----------------------------------------------------------------------

plt.figure()
plt.plot(np.arange(10))
plt.gca().invert_yaxis()

# ----------------------------------------------------------------------
# Heat maps and contour plots
# ----------------------------------------------------------------------

points = np.arange(-5, 5, 0.01)
fnt = {'fontsize': 11}

# Create a grid of points
xs, ys = np.meshgrid(points, points)

# Simple functions for plotting
z = np.sqrt(xs ** 2 + ys ** 2)
z2 = np.sqrt(((xs-2)/2)**2 + (ys-2)**2)
plt.figure(figsize=(10,8))
plt.suptitle('$\sqrt{x^2 + y^2}$ for a grid of values')

# Heatmap with pcolormesh
plt.subplot(221)
plt.pcolormesh(xs, ys, z, cmap='jet')
plt.colorbar()
plt.axis([-5, 5, -5, 5])
plt.title('pcolormesh', fnt)

# Filled contour plot of the same data
plt.subplot(222)
plt.contourf(xs, ys, z, cmap='jet')
plt.colorbar()
plt.title('contourf with defaults', fnt)

# Filled contour plot with specified number of levels
plt.subplot(223)
plt.contourf(xs, ys, z, 20, cmap='jet')
plt.colorbar()
plt.title('contourf with N=20', fnt)

# Filled contour plot with specified contour levels
plt.subplot(224)
plt.contourf(xs, ys, z, np.arange(0.,9.,0.5), cmap='jet')
plt.colorbar()
# -- Add some contour lines
plt.contour(xs,ys,z2,10,colors='black')
plt.title('contourf with V=0,0.5,1,...8.5\n and z2 contour N=10', fnt)

# ----------------------------------------------------------------------
# Quiver plots
# ----------------------------------------------------------------------

# Read a netCDF file into an xray dataset, and unpack into numpy arrays:
with xray.open_dataset('data/ncep2_climatology_ann.nc') as ds:
    lat = ds['lat'].values
    lon = ds['lon'].values
    lev = ds['lev'].values
    u = ds['u'].values
    v = ds['v'].values

# Extract 200mb winds and subsample so vectors aren't too crowded
k = 9   # 200 mb vertical level
nx, ny = 6, 3
uplot, vplot = u[k,::ny,::nx], v[k,::ny,::nx]
xi, yi = np.meshgrid(lon[::nx],lat[::ny])

# Create quiver plot of wind vectors
plt.figure()
plt.quiver(xi, yi, uplot, vplot)

# ----------------------------------------------------------------------
# Basemap
# ----------------------------------------------------------------------

heading('basemap: Plotting geographic data')

print("""\
These examples use the Basemap class from the basemap package which was
imported at the beginning of this module.
""")

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
x, y = -30, 20
m.plot(x, y, latlon=True, marker='*', color='b')
# Add a bunch of points using m.scatter()
lons = [0, 10, -20, -20]
lats = [0, -10, 40, -20]
m.scatter(lons, lats, latlon=True, marker='D',color='b')
# Add some lines with m.plot()
lons = [-15, -150, -100]
lats = [70, 30, 0]
m.plot(lons, lats, latlon=True, color='m', linewidth=2)

# ----------------------------------------------------------------------
# Plot a lat-lon subset of the world map
lon1, lon2 = 0, 120
lat1, lat2 = -45, 45
xi, yi = np.meshgrid(lon, lat)
k = 9   # 200 mb vertical level

plt.figure()
m = Basemap(llcrnrlon=lon1, llcrnrlat=lat1, urcrnrlon=lon2, urcrnrlat=lat2)
m.drawcoastlines()
m.pcolormesh(xi, yi, u[k], cmap='jet')
m.colorbar()

# Add ticks
ax = plt.gca()
ax.set_xticks(np.arange(lon1, lon2, 15))
ax.set_xticklabels([])
ax.set_yticks(np.arange(lat1, lat2, 15))
ax.set_yticklabels([])

# Add nicely formatted ticklabels from basemap
m.drawmeridians(np.arange(0,360,15), labels=[1,0,0,1], labelstyle='E/W',
                linewidth=0.0)
m.drawparallels(np.arange(-90,90,15), labels=[1,0,0,1], labelstyle='N/S',
                linewidth=0.0)
plt.draw()
