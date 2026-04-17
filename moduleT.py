# ==========================================================
# IMPORT STATEMENTS IN PYTHON
# ==========================================================

# ------------------------------------------
# 1. import module
# ------------------------------------------

import math

print(math.sqrt(16))


# ------------------------------------------
# 2. import with alias
# ------------------------------------------

import math as m

print(m.pi)


# ------------------------------------------
# 3. from ... import
# ------------------------------------------

from math import sqrt, pi

print(sqrt(25))
print(pi)


# ------------------------------------------
# 4. from ... import *
# ------------------------------------------

# imports all public names (NOT recommended)

from math import *

print(sqrt(36))


# ==========================================================
# LOCATING MODULE
# ==========================================================

# Python searches modules in:
# 1. Current directory
# 2. PYTHONPATH (environment variable)
# 3. Standard library directories

import sys

print(sys.path)   # shows search paths


# ==========================================================
# MODULE ATTRIBUTES
# ==========================================================

import math

# __file__ → file location (not available for built-in modules sometimes)
print(getattr(math, "__file__", "Built-in module"))

# __package__ → package name
print(math.__package__)

# __doc__ → documentation string
print(math.__doc__[:100])   # first 100 chars

# __dict__ → namespace dictionary
print(list(math.__dict__.keys())[:10])

# __name__ → module name
print(math.__name__)


# ==========================================================
# __name__ == "__main__"
# ==========================================================

# used to check if file is run directly

def main():
    print("Running as main program")

if __name__ == "__main__":
    main()


# ==========================================================
# PACKAGES IN PYTHON
# ==========================================================

# A package is a folder containing modules and __init__.py

# Example structure:
#
# mypackage/
# ├── __init__.py
# ├── module1.py
# └── module2.py


# ------------------------------------------
# IMPORTING FROM PACKAGE
# ------------------------------------------

# import entire module
# import mypackage.module1

# from package import module
# from mypackage import module1

# import specific function
# from mypackage.module1 import func


# ------------------------------------------
# USING __init__.py
# ------------------------------------------

# __init__.py can control package imports

# Example (__init__.py):
# from .module1 import func1
# from .module2 import func2

# then:
# from mypackage import func1


# ==========================================================
# RELATIVE IMPORTS (INSIDE PACKAGE)
# ==========================================================

# from . import module1        # same folder
# from .. import module2       # parent folder


# ==========================================================
# SUMMARY (IN COMMENTS)
# ==========================================================

# import:
#   import module

# from import:
#   from module import name

# from *:
#   imports all (avoid)

# module attributes:
#   __file__, __package__, __doc__, __dict__, __name__

# locating module:
#   sys.path

# package:
#   folder with __init__.py