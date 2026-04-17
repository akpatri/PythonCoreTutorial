# ==========================================================
# ARITHMETIC OPERATORS
# ==========================================================

a = 10
b = 20

print(a + b)   # Addition → 30
print(a - b)   # Subtraction → -10
print(a * b)   # Multiplication → 200
print(b / a)   # Division → 2.0
print(b % a)   # Modulus → 0
print(a ** 2)  # Exponent → 100
print(9 // 2)  # Floor division → 4


# ==========================================================
# COMPARISON (RELATIONAL) OPERATORS
# ==========================================================

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


# ==========================================================
# ASSIGNMENT OPERATORS
# ==========================================================

x = 10

x += 5    # x = x + 5
x -= 2    # x = x - 2
x *= 3    # x = x * 3
x /= 2    # x = x / 2
x %= 4    # x = x % 4
x **= 2   # x = x ** 2
x //= 2   # x = x // 2

# bitwise assignment
x &= 3
x |= 2
x ^= 1
x <<= 1
x >>= 1

print(x)


# ==========================================================
# LOGICAL OPERATORS
# ==========================================================

a = True
b = False

print(a and b)   # False
print(a or b)    # True
print(not a)     # False


# ==========================================================
# BITWISE OPERATORS
# ==========================================================

a = 5   # 0101
b = 3   # 0011

print(a & b)   # AND → 1
print(a | b)   # OR  → 7
print(a ^ b)   # XOR → 6
print(~a)      # NOT → -6
print(a << 1)  # left shift → 10
print(a >> 1)  # right shift → 2


# ==========================================================
# MEMBERSHIP OPERATORS
# ==========================================================

lst = [1, 2, 3]

print(2 in lst)        # True
print(5 not in lst)    # True


# ==========================================================
# IDENTITY OPERATORS
# ==========================================================

x = [1, 2]
y = [1, 2]
z = x

print(x is y)       # False (different objects)
print(x is z)       # True  (same object)
print(x is not y)   # True


# ==========================================================
# OPERATOR PRECEDENCE
# ==========================================================

# highest → lowest priority

result = 2 + 3 * 4 ** 2
# step1: 4**2 = 16
# step2: 3*16 = 48
# step3: 2+48 = 50

print(result)


# ==========================================================
# WALRUS OPERATOR (:=)
# ==========================================================

# assigns value and returns it in same expression

# example in if
if (n := 5) > 3:
    print("n is", n)

# example in loop
numbers = [1, 2, 3, 4]

while (length := len(numbers)) > 0:
    print("Length:", length)
    numbers.pop()


# ==========================================================
# SUMMARY (IN COMMENTS)
# ==========================================================

# Arithmetic: + - * / % ** //
# Comparison: == != > < >= <=
# Assignment: = += -= *= ...
# Logical: and or not
# Bitwise: & | ^ ~ << >>
# Membership: in, not in
# Identity: is, is not

# Precedence:
#   ** highest → logical lowest

# Walrus (:=):
#   assign + use in same expression