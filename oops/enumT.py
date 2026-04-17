# ==========================================================
# ENUMS IN PYTHON
# ==========================================================

# Enum is used to define a set of named constant values

from enum import Enum


# ==========================================================
# 1. CREATING AN ENUM
# ==========================================================

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# ==========================================================
# 2. ACCESSING ENUM MEMBERS
# ==========================================================

# Access by name
print(Color.RED)
print(Color.GREEN)

# Access by value
print(Color(1))   # Color.RED


# ==========================================================
# 3. ACCESSING MODES (VALUE & NAME)
# ==========================================================

c = Color.RED

# value mode
print(c.value)   # 1

# name mode
print(c.name)    # "RED"


# ==========================================================
# 4. ITERATING THROUGH ENUM
# ==========================================================

for color in Color:
    print(color)         # Color.RED, Color.GREEN, Color.BLUE
    print(color.name)    # RED, GREEN, BLUE
    print(color.value)   # 1, 2, 3


# ==========================================================
# 5. COMPARISON
# ==========================================================

print(Color.RED == Color.RED)   # True
print(Color.RED == Color.BLUE)  # False


# ==========================================================
# 6. UNIQUE ENUM VALUES
# ==========================================================

# @unique ensures no duplicate values

from enum import unique

@unique
class Status(Enum):
    SUCCESS = 1
    FAILURE = 2


# ==========================================================
# 7. ENUM WITH STRING VALUES
# ==========================================================

class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


print(Direction.NORTH.value)  # "N"


# ==========================================================
# 8. ACCESS USING STRING NAME
# ==========================================================

print(Color["RED"])   # Color.RED


# ==========================================================
# 9. ENUM IN CONDITIONALS
# ==========================================================

color = Color.GREEN

if color == Color.RED:
    print("Red selected")
elif color == Color.GREEN:
    print("Green selected")


# ==========================================================
# 10. ENUM AUTO VALUES
# ==========================================================

from enum import auto

class AutoEnum(Enum):
    A = auto()
    B = auto()
    C = auto()

print(AutoEnum.A.value)  # auto assigned (1,2,3...)


# ==========================================================
# SUMMARY (IN COMMENTS)
# ==========================================================

# Enum:
#   defines named constants

# Access:
#   Color.RED
#   Color(1)
#   Color["RED"]

# Modes:
#   .value → gives value
#   .name  → gives name

# Iteration:
#   for item in EnumClass

# Benefits:
#   readable, fixed values, safer than raw constants