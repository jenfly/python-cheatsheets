### Contents

This document summarizes my development environment and workflow for Python:

1. Development Environment Overview
2. Initial Setup & Configuration  
3. Creating a New Project
4. Workflow
5. Development Approach

-------
### 1. Development Environment Overview

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
netCDF instructions TBD

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
    'ctrl-k': 'editor:delete-to-end-of-line'
```

Add to ~/.atom/snippets.cson:
```
'.source.python':
    'line':
    'prefix': '--'
    'body': '# ----------------------------------------------------------'
```
##### Markdown Here
For nice README files, save as .md (Markdown Here format).

`Ctrl-Shift-m` to open/close Markdown Here preview window in Atom.

-----------
#### IPython

Included in Anaconda distribution

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

On github.com -- create new repo project1 and get its url

On local machine, link up with github.com repo and push changes:
```
git remote add origin https://...
git push -u origin master
```
After initial setup of remote, can just use ```git push```

Let's say I added a README.md file on github.com in the browser. To merge the online change with my local version:
```
git merge origin/master
```
--------------
### 4. Workflow

* IPython shell and text editor open in adjacent windows
* Edit source code in text editor and run in IPython using %run or %cpaste to run code snippets within IPython


Pasting commands into ipython.

Running scripts within ipython

----------------
### 5. Development Approach
