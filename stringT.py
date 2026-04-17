# stringT.py

# -------------------------------
# SINGLE, DOUBLE, TRIPLE QUOTES
# -------------------------------

s1 = 'Hello'              # single quotes
s2 = "Hello"              # double quotes
s3 = '''Hello
World'''                  # triple quotes (multi-line)
s4 = """Hello
World"""                  # triple quotes (multi-line)

# quotes inside strings
q1 = "It's Python"        # no escape needed
q2 = 'It\'s Python'       # escaped single quote

# -------------------------------
# ACCESSING VALUES IN STRINGS
# -------------------------------

s = "Python"

print(s[0])               # P (index starts at 0)
print(s[1])               # y
print(s[-1])              # n (last character)
print(s[-2])              # o

# -------------------------------
# UPDATING STRINGS (IMMUTABLE)
# -------------------------------

# s[0] = 'J'              # ERROR: strings are immutable

s_new = 'J' + s[1:]       # create new string
print(s_new)              # Jython

# -------------------------------
# ESCAPE CHARACTERS
# -------------------------------

print("Hello\nWorld")     # newline
print("Hello\tWorld")     # tab
print("Hello\\World")     # backslash
print("Hello\'World")     # single quote
print("Hello\"World")     # double quote

# raw string (ignores escape meaning)
print(r"Hello\nWorld")    # prints \n literally

# -------------------------------
# STRING OPERATORS
# -------------------------------

a = "Hello"
b = "Python"

print(a + b)              # concatenation -> HelloPython
print(a * 2)              # repetition -> HelloHello
print(a[1])               # e
print(a[1:4])             # ell

print("H" in a)           # True
print("M" not in a)       # True

# -------------------------------
# STRING FORMATTING
# -------------------------------

name = "John"
age = 25

print("Name: %s Age: %d" % (name, age))   # old style
print("Name: {} Age: {}".format(name, age))  # format()
print(f"Name: {name} Age: {age}")         # f-string (modern)

# formatting numbers
print("%f" % 3.14)        # float
print("%d" % 10)          # integer
print("%x" % 255)         # hex

# -------------------------------
# NEGATIVE & POSITIVE INDEXING
# -------------------------------

s = "Python"

# positive indexing:  0 1 2 3 4 5
# negative indexing: -6-5-4-3-2-1

print(s[0])               # P
print(s[-1])              # n

# -------------------------------
# STRING SLICING
# -------------------------------

s = "Python"

print(s[0:4])             # Pyth
print(s[:4])              # Pyth (start default = 0)
print(s[2:])              # thon (end default = len)
print(s[:])               # Python (full copy)

# step slicing
print(s[::2])             # Pto
print(s[::-1])            # nohtyP (reverse)

# -------------------------------
# NEGATIVE SLICING
# -------------------------------

print(s[-4:-1])           # tho
print(s[-3:])             # hon

# -------------------------------
# DEFAULT VALUES IN SLICING
# -------------------------------

# s[start:end:step]
# default start = 0
# default end = len(s)
# default step = 1

print(s[::])              # Python

# -------------------------------
# RETURN TYPE OF SLICING
# -------------------------------

result = s[1:4]
print(result)             # yth
print(type(result))       # <class 'str'>

# -------------------------------
# BUILT-IN STRING METHODS
# -------------------------------

s = "hello python"

print(s.capitalize())     # Hello python
print(s.upper())          # HELLO PYTHON
print(s.lower())          # hello python
print(s.title())          # Hello Python

print(s.count("o"))       # count occurrences
print(s.find("py"))       # index or -1
print(s.replace("python", "world"))  # replace text

print(s.split())          # ['hello', 'python']
print("-".join(['a','b','c']))  # a-b-c

print(s.startswith("he")) # True
print(s.endswith("on"))   # True

print(s.strip())          # remove spaces

# -------------------------------
# BUILT-IN FUNCTIONS
# -------------------------------

s = "Python"

print(len(s))             # length -> 6
print(max(s))             # highest char -> y
print(min(s))             # lowest char -> P