# ==========================================================
# INPUT IN PYTHON
# ==========================================================

# ------------------------------------------
# 1. input() FUNCTION
# ------------------------------------------

# input() always returns STRING

name = input("Enter your name: ")
print("Hello", name)

# converting input to integer
age = int(input("Enter age: "))
print(age + 5)


# ------------------------------------------
# 2. raw_input() FUNCTION
# ------------------------------------------

# raw_input() was used in Python 2
# In Python 3, input() behaves like raw_input()

# Python 2 example (NOT valid in Python 3):
# name = raw_input("Enter name: ")


# ==========================================================
# OUTPUT FORMATTING IN PYTHON
# ==========================================================

name = "Alice"
age = 25


# ------------------------------------------
# 1. STRING MODULO OPERATOR (%)
# ------------------------------------------

print("Name: %s Age: %d" % (name, age))


# ------------------------------------------
# 2. format() METHOD
# ------------------------------------------

print("Name: {} Age: {}".format(name, age))

# with index
print("Age: {1} Name: {0}".format(name, age))

# with keyword
print("Name: {n} Age: {a}".format(n=name, a=age))


# ------------------------------------------
# 3. f-STRINGS (BEST & MODERN)
# ------------------------------------------

print(f"Name: {name} Age: {age}")

# expressions inside f-string
print(f"Next year age: {age + 1}")


# ------------------------------------------
# 4. TEMPLATE STRINGS
# ------------------------------------------

from string import Template

t = Template("Name: $name Age: $age")

print(t.substitute(name="Alice", age=25))

# safe substitute (avoids error if missing key)
print(t.safe_substitute(name="Bob"))


# ==========================================================
# EXTRA FORMATTING OPTIONS
# ==========================================================

# number formatting
pi = 3.14159
print(f"{pi:.2f}")   # 2 decimal places

# alignment
print(f"{name:>10}")   # right align
print(f"{name:<10}")   # left align
print(f"{name:^10}")   # center align


# ==========================================================
# SUMMARY (IN COMMENTS)
# ==========================================================

# INPUT:
#   input() → takes user input (string)
#   raw_input() → Python 2 only

# OUTPUT FORMATTING:
#   % operator → old style
#   format() → flexible
#   f-string → modern, readable, fastest
#   Template → useful for dynamic templates

# BEST PRACTICE:
#   use f-strings in modern Python