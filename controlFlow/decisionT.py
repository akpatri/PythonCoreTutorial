# ============================================
# DECISION MAKING IN PYTHON
# ============================================

# --------------------------------------------
# 1. if, elif, else
# --------------------------------------------

x = 10

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")


# multiple conditions

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# --------------------------------------------
# 2. NESTED DECISION
# --------------------------------------------

num = 15

if num > 0:
    print("Positive number")
    
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

else:
    print("Negative number")


# --------------------------------------------
# 3. match-case (Python 3.10+)
# --------------------------------------------

# similar to switch-case in other languages

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")


# pattern matching example

value = ("apple", 10)

match value:
    case ("apple", qty):
        print("Apple quantity:", qty)
    case ("banana", qty):
        print("Banana quantity:", qty)
    case _:
        print("Unknown item")


