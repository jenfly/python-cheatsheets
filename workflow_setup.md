

# Git Setup

## Initial configuration

On my local machine:

git config user.name "Jennifer Walker"
git config user.email "jenfly@gmail.com"

Create file ~/.gitignore_global, with files to be ignored, one per line e.g.:
*.pyc
*.pyo
*.log
*~

Tell git to ignore all matching files:
git config --global core.excludesfile ~/.gitignore_global


## Creating a new project

On my local machine:
git init project1
** Add some .py and .txt files to project1 folder **
git add *.txt *.py
git status
git commit -m "My first commit"

On github.com:
Create new repo project1 and get its url

On local machine, link up with github.com and push changes:
git remote add origin https://...
git push -u origin master

Let's say I added a README.md file on github.com in the browser.
To merge the online change with my local version:
git merge origin/master

##
