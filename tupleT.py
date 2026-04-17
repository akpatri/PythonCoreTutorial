# tupleT.py

# -------------------------------
# CREATING TUPLES
# -------------------------------

t1 = (1, 2, 3)            # normal tuple
t2 = ('a', 'b', 'c')

t3 = (5,)                 # single element tuple (comma is required)
t4 = 5,                   # also tuple without parentheses

print(type(t3))           # <class 'tuple'>

# -------------------------------
# ACCESSING VALUES IN TUPLES
# -------------------------------

t = ('spam', 'Spam', 'SPAM!')

print(t[0])               # spam (index starts at 0)
print(t[2])               # SPAM!
print(t[-1])              # SPAM! (last element)
print(t[-2])              # Spam

# -------------------------------
# SLICING TUPLES
# -------------------------------

print(t[1:])              # ('Spam', 'SPAM!')
print(t[:2])              # ('spam', 'Spam')
print(t[:])               # full tuple
print(t[::-1])            # reverse tuple

# -------------------------------
# UPDATING TUPLES (IMMUTABLE)
# -------------------------------

# t[0] = 'new'            # ERROR: tuples are immutable

# workaround: create new tuple
t_new = ('new',) + t[1:]
print(t_new)              # ('new', 'Spam', 'SPAM!')

# -------------------------------
# DELETE TUPLE ELEMENTS
# -------------------------------

# del t[0]                # ERROR: cannot delete individual element

# delete entire tuple
temp = (1, 2, 3)
del temp                 # tuple deleted
# print(temp)            # ERROR: temp is not defined

# -------------------------------
# TUPLE OPERATIONS
# -------------------------------

# concatenation
print((1, 2, 3) + (4, 5, 6))   # (1, 2, 3, 4, 5, 6)

# repetition
print(('Hi!',) * 4)            # ('Hi!', 'Hi!', 'Hi!', 'Hi!')

# membership
print(3 in (1, 2, 3))          # True
print(5 not in (1, 2, 3))      # True

# -------------------------------
# NO ENCLOSING DELIMITERS
# -------------------------------

print('abc', -4.24e93, 18+6.6j, 'xyz')   # tuple-like output

x, y = 1, 2               # tuple unpacking
print("Value of x , y :", x, y)

# -------------------------------
# INDEXING EXAMPLE
# -------------------------------

L = ('spam', 'Spam', 'SPAM!')

print(L[2])               # SPAM!
print(L[-2])              # Spam
print(L[1:])              # ('Spam', 'SPAM!')

# -------------------------------
# BUILT-IN FUNCTIONS WITH TUPLES
# -------------------------------

t = (10, 20, 30, 5)

print(len(t))             # 4
print(max(t))             # 30
print(min(t))             # 5

# convert list to tuple
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)                # (1, 2, 3)

# -------------------------------
# NOTE ON cmp()
# -------------------------------

# cmp() is NOT available in Python 3
# Instead, use comparison operators:

print((1, 2, 3) == (1, 2, 3))   # True
print((1, 2, 3) < (1, 2, 4))    # True