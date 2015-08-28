"""
Jennifer's scientific computing cheatsheet - fancy formatting for plots.

Contents:
- Formatting examples
- Styles

This cheatsheet is all about making plots pretty.  For the basics of
how to create different types of plots, see science_plots.py

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

heading('Making plots pretty')
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Formatting examples
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Styles
# ----------------------------------------------------------------------

# To see a list of built-in styles from matplotlib:
print(plt.style.available)

# To use a style
plt.figure()
plt.style.use('ggplot')
plt.plot(np.arange(10))

# Create your own styles, e.g. presentation, article
# Compose styles together
# plt.style.use(['dark_background', 'presentation'])
