'''
Jennifer's cheatsheet for scientific computing with Python - plotting with
matplotlib and basemap.
- matplotlib basics
- Subplots
- Histograms
- Annotations

Each section of this cheatsheet can be copy/pasted into ipython (using the
%paste magic command for indented code) and run separately in an interactive
session.

Many of these code snippets are pilfered / adapted from:
- Matplotlib documentation
  http://matplotlib.org/users/pyplot_tutorial.html
- Matplotlib tutorial
  http://www.labri.fr/perso/nrougier/teaching/matplotlib/
- Basemap tutorial
  https://basemaptutorial.readthedocs.org/en/latest/index.html

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

# Additional modules useful for atmospheric science
from mpl_toolkits.basemap import Basemap
import xray

# ----------------------------------------------------------------------
print("\nWelcome to Jennifer's cheatsheet for scientific computing in Python!")

def heading(s):
    '''Prints a nice heading to the console.'''
    line = '-' *60
    print('\n' + line + '\n' + s + '\n' + line)

heading('Plotting with matploblib and basemap')
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# matplotlib basics
# ----------------------------------------------------------------------

heading('matplotlib:  2-D plots and visualizations')

print('''\
When running a script in ipython, the figures usually aren't visible when
the script completes.  To show them:
plt.show()

Other operations with figure windows:
plt.figure()        # Creates a new figure window
plt.clf()           # Clears the current figure
plt.cla()           # Clears the current axes
plt.close(1)        # Closes figure 1
plt.close('all')    # Closes all open figure windows
''')

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

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()

# plt.subplot(numrows, numcols, numfig)
plt.subplot(2, 1, 1)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# The commas can be omitted in subplot() if numrows, numcols and numfig
# are all less than 10
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

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

# Playing around with pcolormesh and contourf
x = np.arange(-5, 5)
y = x
xi, yi = np.meshgrid(x, y)
zi = np.random.randn(10, 10)
plt.figure()
plt.pcolormesh(xi, yi, zi)
plt.colorbar()
plt.figure()
plt.contourf(xi, yi, zi)
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
