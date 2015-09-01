"""
Styles and conventions to keep my code consistent.
"""

# ----------------------------------------------------------------------
# Highlights from PEP0008 Style Guide for Python
# ----------------------------------------------------------------------

print("""
PEP8 Highlights
- 4 spaces per indent
- Max line length: 79 characters (72 for docstrings)
- 2 blank lines around top-level function and class definitions
- 1 blank line around method definitions within a class
- Use double quotation marks " in triple-quoted docstrings to be
  consistent with PEP257
- Continuation lines - 2 options:
    a) Aligned with opening delimiter, or
    b) Hanging indent with no arguments on the first line, and further
       indentation to distinguish itself as a continuation line (can be
       other than 4 space indent)
""")

# Continuation lines
# -- Option a)
def my_long_function_name(long_variable_one='hello', long_variable_two=True,
                          long_variable_three=123):
    print('Hello world!')

# -- Option b)
def another_long_function(
        long_variable_one='hello', long_variable_two=True,
        long_variable_three=123):
    if long_variable_two:
        print('Kittens!')

foo = another_long_function(
    long_variable_one='world', long_variable_two=False,
    long_variable_three=100)


# ----------------------------------------------------------------------
# Docstring template
# ----------------------------------------------------------------------
def docstrings(x, n, condition=True, opt='opt1', descrip=None):
    """
    Provide a template for docstring style conventions.

    The first line of a docstring should be a concise summary,
    describing what the function does as an action, e.g.
    - Return the square of a number.
    - Find the unique elements of an array.
    - Load a dataset from a netCDF file.

    If including more than one line in a docstring, the first line
    should be followed by a blank line, then additional details on the
    subsequent lines.  Maximum line length should be 72 characters.

    For the listing of function arguments, I use the following style:
    argname : Variable type or list of acceptable values[, optional]
        Desription of the argument.

    To see this docstring template, call style.docstrings?.

    Parameters
    ----------
    x : float or 1-D sequence of floats
        The data values to frobnicate.
    n : int
        Number of times to biz the baz.

    """

x : array_like
    The x-coordinates of the interpolated values.

xp : 1-D sequence of floats
    The x-coordinates of the data points, must be increasing.

fp : 1-D sequence of floats
    The y-coordinates of the data points, same length as `xp`.


group : str, optional
    Path to the netCDF4 group in the given file to open (only works for
    netCDF4 files).
decode_cf : bool, optional
    Whether to decode these variables, assuming they were saved according
    to CF conventions.
engine : {'netcdf4', 'scipy', 'pydap', 'h5netcdf'}, optional
    Engine to use when reading netCDF files. If not provided, the default
    engine is chosen based on available dependencies, with a preference for
    'netcdf4'.


Parameters
----------
filename_or_obj : str, file or xray.backends.*DataStore
    Strings are interpreted as a path to a netCDF file or an OpenDAP URL
    and opened with python-netCDF4, unless the filename ends with .gz, in
    which case the file is gunzipped and opened with scipy.io.netcdf (only
    netCDF3 supported). File-like objects are opened with scipy.io.netcdf
    (only netCDF3 supported).
group : str, optional
    Path to the netCDF4 group in the given file to open (only works for
    netCDF4 files).
decode_cf : bool, optional
    Whether to decode these variables, assuming they were saved according
    to CF conventions.
mask_and_scale : bool, optional
    If True, replace array values equal to `_FillValue` with NA and scale
    values according to the formula `original_values * scale_factor +
    add_offset`, where `_FillValue`, `scale_factor` and `add_offset` are
    taken from variable attributes (if they exist).
decode_times : bool, optional
    If True, decode times encoded in the standard NetCDF datetime format
    into datetime objects. Otherwise, leave them encoded as numbers.
concat_characters : bool, optional
    If True, concatenate along the last dimension of character arrays to
    form string arrays. Dimensions will only be concatenated over (and
    removed) if they have no corresponding variable and if they are only
    used as the last dimension of character arrays.
decode_coords : bool, optional
    If True, decode the 'coordinates' attribute to identify coordinates in
    the resulting dataset.
engine : {'netcdf4', 'scipy', 'pydap', 'h5netcdf'}, optional
    Engine to use when reading netCDF files. If not provided, the default
    engine is chosen based on available dependencies, with a preference for
    'netcdf4'.
chunks : dict, optional
    If chunks is provided, it used to load the new dataset into dask
    arrays. This is an experimental feature; see the documentation for more
    details.
lock : False, True or threading.Lock, optional
    If chunks is provided, this argument is passed on to
    :py:func:`dask.array.from_array`. By default, a per-variable lock is
    used when reading data from netCDF files with the netcdf4 and h5netcdf
    engines to avoid issues with concurrent access when using dask's
    multithreaded backend.
   engine is chosen based on available dependencies, with a preference for
    'netcdf4'.
chunks : dict, optional
    If chunks is provided, it used to load the new dataset into dask
    arrays. This is an experimental feature; see the documentation for more
    details.
lock : False, True or threading.Lock, optional
    If chunks is provided, this argument is passed on to
    :py:func:`dask.array.from_array`. By default, a per-variable lock is
    used when reading data from netCDF files with the netcdf4 and h5netcdf
    engines to avoid issues with concurrent access when using dask's
    multithreaded backend.

Returns
-------
dataset : Dataset
    The newly created dataset.

See Also
--------
open_mfdataset



Parameters
----------
x : array_like
    The x-coordinates of the interpolated values.

xp : 1-D sequence of floats
    The x-coordinates of the data points, must be increasing.

fp : 1-D sequence of floats
    The y-coordinates of the data points, same length as `xp`.

left : float, optional
    Value to return for `x < xp[0]`, default is `fp[0]`.

right : float, optional
    Value to return for `x > xp[-1]`, default is `fp[-1]`.

Returns
-------
y : {float, ndarray}
    The interpolated values, same shape as `x`.

Raises
------
ValueError
    If `xp` and `fp` have different length

Notes
-----
Does not check that the x-coordinate sequence `xp` is increasing.
If `xp` is not increasing, the results are nonsense.
A simple check for increasing is::

    np.all(np.diff(xp) > 0)


Examples
--------
>>> xp = [1, 2, 3]



Parameters
----------
objs : sequence of Dataset and DataArray objects
    xray objects to concatenate together. Each object is expected to
    consist of variables and coordinates with matching shapes except for
    along the concatenated dimension.
dim : str or DataArray or pandas.Index
    Name of the dimension to concatenate along. This can either be a new
    dimension name, in which case it is added along axis=0, or an existing
    dimension name, in which case the location of the dimension is
    unchanged. If dimension is provided as a DataArray or Index, its name
    is used as the dimension to concatenate along and the values are added
    as a coordinate.
data_vars : {'minimal', 'different', 'all' or list of str}, optional
    These data variables will be concatenated together:
      * 'minimal': Only data variables in which the dimension already
        appears are included.
      * 'different': Data variables which are not equal (ignoring
       attributes) across all datasets are also concatenated (as well as
        all for which dimension already appears). Beware: this option may
        load the data payload of data variables into memory if they are not
        already loaded.
      * 'all': All data variables will be concatenated.
      * list of str: The listed data variables will be concatenated, in
        addition to the 'minimal' data variables.
    If objects are DataArrays, data_vars must be 'all'.
coords : {'minimal', 'different', 'all' o list of str}, optional
    These coordinate variables will be concatenated together:
      * 'minimal': Only coordinates in which the dimension already appears
        are included.
      * 'different': Coordinates which are not equal (ignoring attributes)
        across all datasets are also concatenated (as well as all for which
        dimension already appears). Beware: this option may load the data
        payload of coordinate variables into memory if they are not already
        loaded.
      * 'all': All coordinate variables will be concatenated, except
        those corresponding to other dimensions.
      * list of str: The listed coordinate variables will be concatenated,
        in addition the 'minimal' coordinates.
compat : {'equals', 'identical'}, optional
    String indicating how to compare non-concatenated variables and
Returns
-------
concatenated : type of objs

See also
--------
auto_combine
