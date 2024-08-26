# woodchipper-git-ignore
A simple python script for quick adding .gitignore from the commandline

## Setup
Simply run gignore.py after installing python3

## Usage
gignore supports the following command-line interfaces:

```shell 
gignore -s: Creates the .gitignore file if necessary and adds .wcn* to it.
gignore -s python: Creates the .gitignore file if necessary and adds .wcn*, .idea, __pycache__
gignore -a [target]: Creates the .gitignore file if necessary and adds target to it.
gignore -r [target]: IF the .gitignore file exists and contains target, removes target from the file.
gignore -c: Clears the .gitignore file without deleting it, removing every line of text from it. 
```