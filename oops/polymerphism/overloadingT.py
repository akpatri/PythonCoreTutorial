# ==========================================================
# METHOD OVERLOADING IN PYTHON
# ==========================================================

# Python does NOT support traditional method overloading
# (same function name with different parameters like Java/C++)

# If we define multiple methods with same name,
# the last one overrides previous ones

class Demo:
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):   # overrides previous method
        print(a + b + c)

d = Demo()
# d.add(2, 3)  # ERROR (expects 3 arguments)
d.add(1, 2, 3)


# ==========================================================
# WAY 1: SIMULATE OVERLOADING USING DEFAULT ARGUMENTS
# ==========================================================

class Demo:
    def add(self, a, b, c=0):
        print(a + b + c)

d = Demo()
d.add(2, 3)        # works like 2-arg version
d.add(2, 3, 4)     # works like 3-arg version


# ==========================================================
# WAY 2: USING *args (VARIABLE ARGUMENTS)
# ==========================================================

class Demo:
    def add(self, *args):
        print(sum(args))

d = Demo()
d.add(1, 2)
d.add(1, 2, 3, 4)


# ==========================================================
# METHOD OVERLOADING USING MULTIPLE DISPATCH
# ==========================================================

# MultipleDispatch allows function behavior based on argument types

# install library:
# pip install multipledispatch

from multipledispatch import dispatch


class Calculator:

    @dispatch(int, int)
    def add(self, a, b):
        print("int + int =", a + b)

    @dispatch(int, int, int)
    def add(self, a, b, c):
        print("int + int + int =", a + b + c)

    @dispatch(float, float)
    def add(self, a, b):
        print("float + float =", a + b)


calc = Calculator()

calc.add(2, 3)          # matches (int, int)
calc.add(1, 2, 3)       # matches (int, int, int)
calc.add(2.5, 3.5)      # matches (float, float)


# ==========================================================
# IMPORTANT NOTES (IN COMMENTS)
# ==========================================================

# Method Overloading:
#   same method name, different parameters

# Python:
#   does NOT support it directly

# Alternatives:
#   - default arguments
#   - *args
#   - type checking inside function
#   - multipledispatch library

# MultipleDispatch:
#   chooses function based on argument types and count