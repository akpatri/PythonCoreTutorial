# ==========================================================
# CALL BY VALUE vs CALL BY REFERENCE (PYTHON BEHAVIOR)
# ==========================================================

# Python uses "call by object reference" (or call by sharing)

# immutable example (acts like call by value)
def modify(x):
    x = x + 10   # creates new object

a = 5
modify(a)
print(a)   # 5 (unchanged)


# mutable example (acts like call by reference)
def modify_list(lst):
    lst.append(100)   # modifies original object

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)   # [1, 2, 3, 100]


# ==========================================================
# FUNCTION ARGUMENT TYPES
# ==========================================================

# ------------------------------------------
# 1. POSITIONAL (REQUIRED) ARGUMENT
# ------------------------------------------

def add(a, b):
    print(a + b)

add(2, 3)   # order matters


# ------------------------------------------
# 2. KEYWORD ARGUMENT
# ------------------------------------------

add(a=5, b=10)   # order doesn't matter


# ------------------------------------------
# 3. DEFAULT ARGUMENT
# ------------------------------------------

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Alice")


# ------------------------------------------
# 4. POSITIONAL-ONLY ARGUMENT (/)
# ------------------------------------------

def func(a, b, /):
    print(a, b)

func(1, 2)
# func(a=1, b=2)  # ERROR


# ------------------------------------------
# 5. KEYWORD-ONLY ARGUMENT (*)
# ------------------------------------------

def func2(*, x, y):
    print(x, y)

func2(x=10, y=20)
# func2(10, 20)  # ERROR


# ------------------------------------------
# 6. VARIABLE-LENGTH ARGUMENTS
# ------------------------------------------

# *args → tuple of positional args
def sum_all(*args):
    print(args)
    print(sum(args))

sum_all(1, 2, 3, 4)


# **kwargs → dictionary of keyword args
def print_info(**kwargs):
    print(kwargs)

print_info(name="Alice", age=25)


# ==========================================================
# ORDER OF ARGUMENTS
# ==========================================================
# correct order:
# positional → default → *args → keyword-only → **kwargs
def example(a, b=2, *args, c, d=5, **kwargs):
    print(a, b, args, c, d, kwargs)
example(1, 3, 4, 5, c=10, x=100)


# ==========================================================
# FUNCTION ANNOTATION (TYPE HINTS)
# ==========================================================

def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(2, 3))
print(multiply.__annotations__)   # shows type hints


# ==========================================================
# DOCSTRING
# ==========================================================

def square(x):
    """Returns square of a number"""
    return x * x

print(square.__doc__)


# ==========================================================
# ANONYMOUS FUNCTIONS (LAMBDA)
# ==========================================================

# lambda arguments: expression

add = lambda a, b: a + b
result = add(3, 4)
print(result)

# used in functions like map, filter
nums = [1, 2, 3]
squares = list(map(lambda x: x*x, nums))
print(squares)


# ==========================================================
# PACKING ARGUMENTS : normal variable -> list or tuple or dict
# ==========================================================

# *args → packs into tuple
def func(*args):
    print(args)
func(1, 2, 3)  #(1, 2, 3)

# **kwargs → packs into dict
def func2(**kwargs):
    print(kwargs)
func2(name="Asish", age=22) #{'name': 'Asish', 'age': 22}

# ==========================================================
# UNPACKING ARGUMENTS : list or tuple or dict -> normal variable 
# ==========================================================

# unpack list using *
def add(a, b, c):
    print(a + b + c)

lst = [1, 2, 3]
add(*lst)


# unpack dict using **
def show(name, age):
    print(name, age)

d = {"name": "Alice", "age": 25}
show(**d)


# ==========================================================
# COMBINED EXAMPLE
# ==========================================================

def demo(a, *args, **kwargs):
    print("a:", a)
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, x=10, y=20)


# ==========================================================
# SUMMARY (IN COMMENTS)
# ==========================================================

# Call type:
#   Python uses object reference

# Arguments:
#   positional, keyword, default
#   positional-only (/), keyword-only (*)

# Variable args:
#   *args → tuple
#   **kwargs → dict

# Order:
#   positional → default → *args → keyword-only → **kwargs

# Lambda:
#   anonymous one-line function

# Packing:
#   collect arguments

# Unpacking:
#   spread arguments