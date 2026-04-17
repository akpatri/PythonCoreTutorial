# ==========================================================
# CLOSURES IN PYTHON
# ==========================================================

# A closure is a function object that remembers values
# from its enclosing (outer) function even after the outer
# function has finished execution


# ==========================================================
# 1. NESTED FUNCTIONS
# ==========================================================

def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()


# ==========================================================
# 2. ACCESSING ENCLOSING SCOPE
# ==========================================================

def outer():
    x = 10   # enclosing variable

    def inner():
        print("Accessing outer variable:", x)

    inner()

outer()


# ==========================================================
# 3. CREATING A CLOSURE
# ==========================================================

def outer():
    x = 100   # variable to be captured

    def inner():
        print("Captured value:", x)

    return inner   # return inner function (closure)


closure_func = outer()   # outer() finishes execution

closure_func()   # still remembers x = 100


# ==========================================================
# 4. RETENTION OF STATE
# ==========================================================

def counter():
    count = 0

    def increment():
        # count += 1  # ERROR without nonlocal
        print("Count:", count)

    return increment


c = counter()
c()   # always prints 0 (no modification)


# ==========================================================
# 5. nonlocal KEYWORD
# ==========================================================

# used to modify variable from enclosing scope

def counter():
    count = 0

    def increment():
        nonlocal count   # refers to outer variable
        count += 1
        print("Count:", count)

    return increment


c = counter()

c()   # 1
c()   # 2
c()   # 3


# ==========================================================
# 6. MULTIPLE CLOSURES WITH DIFFERENT STATES
# ==========================================================

def make_multiplier(n):
    def multiply(x):
        return x * n   # n is captured
    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15


# ==========================================================
# 7. CHECKING CLOSURE VARIABLES
# ==========================================================

def outer():
    x = 50

    def inner():
        return x

    return inner

f = outer()

print(f.__closure__)         # shows closure cells
print(f.__closure__[0].cell_contents)  # value of x


# ==========================================================
# SUMMARY (IN COMMENTS)
# ==========================================================

# Nested Function:
#   function inside another function

# Closure:
#   inner function that remembers outer variables

# Key Features:
#   - access enclosing scope
#   - retain state after outer function ends

# nonlocal:
#   - used to modify outer (non-global) variable
#   - required for state changes inside closure

# Use Cases:
#   - function factories
#   - maintaining state without global variables