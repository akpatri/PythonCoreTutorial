# ==========================================================
# FUNCTION DECORATORS IN PYTHON
# ==========================================================

# A decorator is a function that modifies another function
# without changing its actual code


# ==========================================================
# BASIC DECORATOR SYNTAX
# ==========================================================

def decorator(func):   # function to be decorated

    def wrapper():
        print("Before function call")
        func()   # original function
        print("After function call")

    return wrapper


# applying decorator manually
def greet():
    print("Hello")

greet = decorator(greet)   # function = decorator(function)
greet()


# ==========================================================
# USING @ SYNTAX (SUGAR)
# ==========================================================

@decorator
def say_hi():
    print("Hi")

say_hi()


# ==========================================================
# DECORATOR WITH ARGUMENTS
# ==========================================================

def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result

    return wrapper


@decorator
def add(a, b):
    return a + b

print(add(2, 3))


# ==========================================================
# CHAINING MULTIPLE DECORATORS
# ==========================================================

def deco1(func):
    def wrapper():
        print("Deco1")
        func()
    return wrapper


def deco2(func):
    def wrapper():
        print("Deco2")
        func()
    return wrapper


@deco1
@deco2
def test():
    print("Function")

# Equivalent to:
# test = deco1(deco2(test))

test()


# ==========================================================
# BUILT-IN DECORATORS
# ==========================================================

# ----------------------------------------------------------
# 1. @classmethod
# ----------------------------------------------------------

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def show_count(cls):   # cls instead of self
        print("Count:", cls.count)


MyClass()
MyClass()
MyClass.show_count()


# ----------------------------------------------------------
# 2. @staticmethod
# ----------------------------------------------------------

class Math:

    @staticmethod
    def add(a, b):
        return a + b


print(Math.add(5, 3))


# ----------------------------------------------------------
# 3. @property
# ----------------------------------------------------------

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):   # getter
        return self._name

    @name.setter
    def name(self, value):   # setter
        self._name = value

    @name.deleter
    def name(self):   # deleter
        del self._name


p = Person("Alice")

print(p.name)   # getter
p.name = "Bob"  # setter
print(p.name)


# ==========================================================
# SUMMARY (IN COMMENTS)
# ==========================================================

# decorator:
#   function that wraps another function

# syntax:
#   function = decorator(function)
#   OR use @decorator

# wrapper function:
#   adds extra behavior

# @classmethod:
#   works with class (cls)

# @staticmethod:
#   independent method (no self/cls)

# @property:
#   used for getter/setter (encapsulation)