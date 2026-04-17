# warningT.py

# -------------------------------
# DISPLAY A WARNING MESSAGE
# -------------------------------

import warnings

warnings.warn("This is a simple warning")   # default UserWarning


# -------------------------------
# TYPES OF WARNING CLASSES
# -------------------------------

warnings.warn("User warning example", UserWarning)

warnings.warn("Deprecated feature", DeprecationWarning)

warnings.warn("Syntax issue", SyntaxWarning)

warnings.warn("Runtime issue", RuntimeWarning)

warnings.warn("Import issue", ImportWarning)


# -------------------------------
# USERWARNING CLASS (DEFAULT)
# -------------------------------

warnings.warn("This is a UserWarning")   # default type


# -------------------------------
# WARNING FILTERS
# -------------------------------

# show only once (default behavior)
warnings.filterwarnings("default")

# always show warnings
warnings.filterwarnings("always")
warnings.warn("Always show this warning")

# ignore warnings
warnings.filterwarnings("ignore")
warnings.warn("This will NOT be shown")

# convert warning into error
warnings.filterwarnings("error")

try:
    warnings.warn("This becomes exception")
except Warning as e:
    print("Caught as exception:", e)


# reset filters
warnings.resetwarnings()


# -------------------------------
# simplefilter (shortcut)
# -------------------------------

warnings.simplefilter("always")
warnings.warn("Simple filter example")


# -------------------------------
# showwarning (custom display)
# -------------------------------

def custom_showwarning(message, category, filename, lineno, file=None, line=None):
    print(f"Custom Warning -> {message} [{category.__name__}]")

warnings.showwarning = custom_showwarning

warnings.warn("Using custom showwarning")


# -------------------------------
# warn_explicit
# -------------------------------

warnings.warn_explicit(
    message="Explicit warning",
    category=UserWarning,
    filename="myfile.py",
    lineno=10
)


# -------------------------------
# EXAMPLE: DEPRECATION WARNING
# -------------------------------

def old_function():
    warnings.warn("old_function is deprecated", DeprecationWarning)

old_function()


# -------------------------------
# EXAMPLE: RUNTIME WARNING
# -------------------------------

def divide(a, b):
    if b == 0:
        warnings.warn("division by zero risk", RuntimeWarning)
    return a / b if b != 0 else None

print(divide(10, 0))






