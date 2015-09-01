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
def docstrings(x, n, spam=True, eggs='green', title=None):
    """
    Return a recipe for breakfast.
    
    This nonsense function provides a template for docstring style
    conventions. To see the template, call `style.docstrings?`.    

    The first line of a docstring should be a concise summary,
    describing what the function does as an action, e.g.,
    - Return the square of a number.
    - Find the unique elements of an array.
    - Load a dataset from a netCDF file.

    If including more than one line in a docstring, the first line
    should be followed by a blank line, then additional details on the
    subsequent lines.  Maximum line length should be 72 characters.

    For the listing of function arguments, I use the following style:

    argname : variable type or list of acceptable values[, optional]
        Desription of the argument.


    Parameters
    ----------
    x : float, list of floats, or ndarray
        The data values to frobnicate.
    n : int
        Number of times to biz the baz.
    spam : bool, optional
        If True, the ham will be spammed.
    eggs : {'green', 'scrambled', 'hard boiled'}, optional
        Type of eggs to include in the recipe.
    title : str, optional
        Title for the recipe.

    Returns
    -------
    recipe : dict
        A delicious recipe for breakfast.

    Raises
    ------
    ValueError
        If `eggs` is not a valid option from the parameter list.

    Notes
    -----
    Does not check that recipe amounts are realistic. Negative values
    in `x` will give nonsense results.

    Examples
    --------
    >>> breakfast = docstrings([2.5, 1.0, 1.3], 2, eggs='scrambled')

    See Also
    --------
    lunch, dinner
    """

    recipe = dict()

    # Do stuff

    return recipe
