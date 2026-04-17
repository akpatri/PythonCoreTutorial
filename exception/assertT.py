# assertT.py

# -------------------------------
# BASIC ASSERT SYNTAX
# -------------------------------

x = 10

assert x > 0             # passes (no error)
# assert x < 0           # fails → AssertionError


# -------------------------------
# ASSERT WITH MESSAGE
# -------------------------------

y = -5

# if condition is False → raises AssertionError with message
# assert y > 0, "y must be positive"


# -------------------------------
# HANDLING AssertionError
# -------------------------------

try:
    z = -1
    assert z > 0, "z must be positive"
except AssertionError as e:
    print("AssertionError caught:", e)


# -------------------------------
# REAL EXAMPLE
# -------------------------------

def divide(a, b):
    assert b != 0, "denominator cannot be zero"
    return a / b

try:
    print(divide(10, 2))     # works
    print(divide(10, 0))     # AssertionError
except AssertionError as e:
    print("Error:", e)


# -------------------------------
# MULTIPLE ASSERTIONS
# -------------------------------

age = 18

try:
    assert age >= 0, "age cannot be negative"
    assert age >= 18, "must be adult"
    print("Valid age")
except AssertionError as e:
    print("Validation failed:", e)


# -------------------------------
# NOTE
# -------------------------------

# assertions are mainly used for debugging
# they can be disabled using python -O (optimized mode)

# python -O assertT.py   → disables all assert statements