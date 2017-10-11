### Contents

This document summarizes my development environment and workflow for Python:

1. Development Environment
2. Initial Setup & Configuration  
3. Creating a New Project
4. Workflow & Daily Operations
5. Development Approach

-------
### 1. Development Environment

Component | Details
------- | --------- |
Python | Python 2.7 Anaconda distribution
Atom | Text editor for .py and other source files
IPython | Enhanced interactive Python shell for scientific computing
Git / GitHub | Version control and code sharing

-----------
### 2. Initial Setup & Configuration

#### Python
Install Anaconda package from Continuum Analytics: http://continuum.io/downloads.
Includes IPython, numpy, matplotlib, scipi, pandas for scientific computing.

Update to latest versions:
```
conda update conda
conda update ipython ipython-notebook ipython-qtconsole
```

##### Install additional libraries
```
conda install basemap netcdf4 xarray dask bottleneck pep8 nltk bokeh sphinx sphinx_rtd_theme proj4
pip install cartopy
```


Add the pep8 checker to the aliases in my `~/.bashrc` file:
```
alias pep8='~/anaconda/bin/pep8'
```

-----------
#### Atom Text Editor

Install from https://atom.io/

##### Editor Configuration
* Preferences -> Settings:
    - "Soft Tabs" on
* Preferences -> Packages -> python-language:
    - "Set Tab Length" = 4
* Preferences -> Packages -> autocomplete-plus:
    - "Keymap for confirming a suggestion" = "tab" only (not tab and enter)
* Preferences -> Packages -> markdown-preview:
    - "GitHub.com style" on

Add to ~/.atom/keymap.cson:
```
'atom-text-editor':
    'ctrl-k': 'editor:cut-to-end-of-line'
```

Add to ~/.atom/snippets.cson:
```
'.source.python':
    'line':
    'prefix': '--'
    'body': '# ----------------------------------------------------------'
```

-----------
#### IPython

Included in Anaconda distribution

##### Matplotlib integration

For my workflow, I always want to launch IPython with the `--matplotlib` option,
so that figure windows work properly, so I add to my aliases in my
`~/.bashrc` file:
```
alias ipython='ipython --matplotlib'
```

Or on Windows, I modify the default IPython profile by setting
`c.InteractiveShellApp.matplotlib = 'auto'` in `ipython_config.py` (located in
 `~/.ipython/profile_default`).  If the file does not already exist, create
 the default profile with `ipython profile create`.

##### Automatic logging of sessions
Set up auto-logging TBD


-----------
#### Git

On my local machine:
```
git config user.name "Jennifer Walker"
git config user.email "jenfly@gmail.com"
```

Create file ~/.gitignore_global, with files to be ignored, one per line e.g.:
```
*.pyc
*.pyo
*.log
*~
```

Tell git to ignore all matching files:
```
git config --global core.excludesfile ~/.gitignore_global
```
------------

### 3. Creating a New Project

#### Git & GitHub

On my local machine:
```
git init project1
** Add some .py and .txt files to project1 folder **
git add *.txt *.py
git status
git commit -m "My first commit"
```

On github.com -- create a new repo called "project1" and get its URL

On local machine, link up with github.com repo and push changes:
```
git remote add origin https://...
git push -u origin master
```
After initial setup of remote, can just use ```git push```


--------------
### 4. Workflow & Daily Operations

#### Source code editing & testing

* Edit source code in text editor
* Launch IPython from the command line in an adjacent
window.
* Test code in the IPython shell.  Two options:
  1. Run the whole script in IPython using `%run foo.py`, or
  2. Copy code snippets from editor and use `%paste` or `%cpaste` to paste
  and run indented code snippets in IPython
* Use Git to commit changes to source code and other project files on at least
a daily basis
* For nice README files, save as .md (Markdown Here format).  Use
`Ctrl-Shift-m` to open/close Markdown Here preview window in Atom.
* To check my code against the PEP8 style guide, run `pep8 foo.py` from
  the command line

#### Python packages and search path

##### Adding Python packages

Use the Anaconda package manager to add a package `newpkg`:
```
conda install newpkg
```

If `newpkg` isn't found in the Anaconda package list, use `pip` to add it.
`pip` is already included in Anaconda.
```
pip install newpkg
```

Installing a package in editable (development) mode:
```
pip install -e <url_or_path>
```
Or within the project directory,
```
python setup.py develop
```

##### Adding to the Python search path

If I've been working on a module `/home/jwalker/fuzzy/kittens.py` and want
to import it from another directory in a Python script or module, I can add
the directory to the Python search path on the fly within Python/IPython:
```
import sys
sys.path.append('/home/jwalker/fuzzy')
import kittens
```

Or I can modify my `.bashrc` or `.cshrc` so that this directory is automatically
added to the Python search path.

* In `~/.bashrc` (home computers):
```
export PYTHONPATH=${PYTHONPATH}:/home/jwalker/fuzzy/
```

* In `~/.cshrc` (school computer):
```
setenv PYTHONPATH ${PYTHONPATH}:/home/jwalker/fuzzy/
```

#### Virtual environments

##### My workflow

* In the project folder, create an `env_init.yml` file with the minimum
specifications for the environment (e.g. environment name, Python version,
list of packages, specific package versions)
* Create the environment with `conda env create -f env_init.yml`
* Save the full details of the environment to an `environment.yml` file with
`conda env export -n myenv > environment.yml` where `myenv` is the environment
name
* Whenever working on the project, first activate the environment with `source
activate myenv` (or `activate myenv` on Windows)
* Whenever adding or updating a package in the environment, update
`environment.yml` by exporting the environment


##### Command reference

To see a list of my conda environments, use `conda env list` or
`conda info --envs`.  The active environment is highlighted with an asterisk.
By default, the active environment is shown in ( ) before the command prompt:
`(myenv) $`.


To activate / deactivate an environment:
```
source activate myenv   # Activate myenv
source deactivate       # Deactivate the current environment
```
On Windows, use `activate myenv` and `deactivate`.

To see a list of all packages installed in a specific environment:
```
conda list -n myenv     # If the environment is not activated
conda list              # If the environment is activated
```

To see if a specific package is installed in an environment:
```
conda list -n myenv scipy
```

To remove an environment:
```
conda remove -n myenv --all
```

Creating an environment:
```
conda create -n myenv           # Uses same Python version as currently in use
conda create -n myenv python=3.4    # Specify Python version
conda create -n myenv scipy         # Include a specific package       
conda install -n myenv scipy        # Install package in existing environment
conda create -n myenv scipy=0.15.0  # Specific version of a package
conda create -n myenv python=3.4 scipy=0.15.0 astroid babel # Multiple packages
conda create -n myclone --clone myenv    # Clone an environment
```

Creating an environment from an `environment.yml` file:
```
conda env create -f environment.yml
```
Example `environment.yml` file:
```
name: myenv
dependencies:
- python=3
- ipython
- numpy
- pip
- pip:
    - pydap==3.2.2
```
Note that versions are specified with a single `=` for conda packages and a
double `==` for pip packages.

Exporting the environment file:
```
source activate myenv
conda env export > environment.yml  # Note: overwrites existing environment.yml
```


#### Git / GitHub operations

##### Commit frequency

Commit changes frequently with descriptive messages.  Ideally, I will commit at
each of the following milestones:
* Added new functionality to existing code
* Added a new file or renamed / reorganized files
* Fixed a bug
* Updated documentation
* End of work day


##### Staging and committing

In my usual workflow I don't need to bother staging changes separately before
committing, so I can skip the staging area using the `-a` option when
committing, which automatically stages every file that is already tracked (does
not include new files that haven't been added to git yet):
```
git commit -a -m "My commit message"
```

If I do want to use the staging area separately, I can stage all modified and
new files for commit using the `-A` option with `git add`:
```
git add -A
git commit -m "My commit message"
```

##### Adding, deleting, and renaming files

To add new files to be tracked in git and stage them for commit:
```
git add file.txt    # Add a specific file
git add *.txt       # Add all .txt files
git add -A          # Add all new and modified files
```

To delete a file:
```
git rm file.txt # Removes file from git
git commit -m "Deleted file.txt" # Deletes file.txt from working directory
```

To rename a file:
```
git mv file.txt file2.txt # Renames in git
git commit -m "Renamed file2.txt" # Renames the file in working directory
```

##### Ignoring files

Create a `.gitignore` file in the project working directory with a
list of project-specific files to ignore in addition to the ignored
files listed in `~/.gitignore_global`.

##### Pulling from server

If I edit project files online in the browser at github.com (e.g. adding a
README.md file), then I want to fetch the online changes and merge with my
local version:
```
git pull origin master
```

##### Reverting to a previous version

Generate a new commit that undoes all of the changes introduced in a commit,
then apply it to the current branch:
```
git revert <commit>
```


##### Handy commands

```
git status  # Current status
git diff    # Changes since last commit
git log     # List of commits
git whatchanged     # List of commits with more details
git whatchanged --since="2 weeks ago"   # Change history last 2 weeks
git config --list # Check your config settings
git revert HEAD   # Revert the last commit
```

----------------
### 5. Development Approach

Incremental milestones and iterative development: Identify first milestone, get
it working, then go on to the next milestone. Use git commits to track.

Test driven development practices?

Agile development practices?

Maintain larger modules, each with high internal cohesion, rather than many
tiny separate files.  Aim for a sensible and intuitive module and package
structure for a large codebase.
