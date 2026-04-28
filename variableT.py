# variableT.py

# -------------------------------
# CREATING VARIABLE
# -------------------------------

x = 10
name = "Python"
a = b = c = 5             # multiple assignment
p, q = 1, 2              # unpacking during assignment

# -------------------------------
# MEMORY ADDRESS
# -------------------------------

print(id(x))             # memory address of x
print(id(name))

# -------------------------------
# PRINTING
# -------------------------------

print(x)
print(name)
print("Value:", x)

# -------------------------------
# DELETING VARIABLE
# -------------------------------

temp = 100
del temp
# print(temp)            # ERROR: variable deleted

# -------------------------------
# GETTING TYPE
# -------------------------------

print(type(x))           # <class 'int'>
print(type(name))        # <class 'str'>

# -------------------------------
# MULTIPLE ARGUMENT (PRINT)
# -------------------------------

print("x =", x, "name =", name)

# -------------------------------
# CONSTANT (CONVENTION)
# -------------------------------

PI = 3.14                # constant (by naming convention)
# PI = 3.1415            # can change but should not

# -------------------------------
# ACCESSIBILITY (OOP)
# -------------------------------

class Demo:
    public_var = "public"

    _protected_var = "protected"      # convention

    __private_var = "private"         # name mangling

    def __init__(self):
        self.value = 10

    # getter
    def get_value(self):
        return self.value

    # setter
    def set_value(self, v):
        self.value = v

d = Demo()

print(d.public_var)        # public
print(d._protected_var)   # accessible but discouraged

# print(d.__private_var)  # ERROR

print(d._Demo__private_var)  # name mangling access

# getter/setter
print(d.get_value())
d.set_value(50)
print(d.get_value())

# -------------------------------
# TYPES OF VARIABLES
# -------------------------------

g = 100                   # global variable

def func():
    l = 10                # local variable
    print(l)

func()
print(g)

# -------------------------------
# DATA TYPES
# -------------------------------

# numeric
i = 10                   # int
f = 3.14                 # float
c = 2 + 3j               # complex

# string
s = "hello"

# sequence
lst = [1, 2, 3]          # list
tup = (1, 2, 3)          # tuple
rng = range(5)           # range

# binary
b = bytes([65, 66])      # byte
ba = bytearray([65, 66]) # bytearray
mv = memoryview(b)       # memoryview

# dictionary
dct = {"a": 1, "b": 2}

# set
st = {1, 2, 3}
fs = frozenset([1, 2, 3])

# boolean
flag = True

# none
n = None

# -------------------------------
# TYPE CASTING
# -------------------------------

# implicit
x = 10
y = 2.5
z = x + y                # int -> float automatically
print(z)

# explicit
print(int("10"))         # string to int
print(float(5))          # int to float
print(complex(2, 3))     # complex
print(str(100))          # to string

print(tuple([1, 2]))     # list -> tuple
print(list((1, 2)))      # tuple -> list
print(set([1, 2, 2]))    # remove duplicates
print(dict([(1, 'a'), (2, 'b')]))

print(chr(65))           # A
print(ord('A'))          # 65
print(hex(255))          # 0xff
print(oct(8))            # 0o10

# eval (use carefully)
print(eval("2 + 3"))     # 5

# -------------------------------
# PACKING AND UNPACKING
# -------------------------------

# packing
t = 1, 2, 3              # tuple packing

# unpacking
a, b, c = t
print(a, b, c)

# extended unpacking (* for remaining elements)
t = (10, 20, 30, 40, 50, 60)
x, *y, z = t
print(x)  # first value
print(y)  # middle values
print(z)  # last value