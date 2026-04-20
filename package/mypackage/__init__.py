print("mypackage __init__ executing")

# expose selected names to package namespace
from .math import add
from .info import name

# define what * import should bring
__all__ = ["add", "name"]

# package-level variable
package_var = "I am inside package"