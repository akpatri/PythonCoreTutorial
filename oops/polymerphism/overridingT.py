# ==========================================================
# POLYMORPHISM IN PYTHON
# ==========================================================

# Polymorphism = "many forms"
# Same interface (method/operator) behaves differently


# ==========================================================
# 1. DUCK TYPING
# ==========================================================

# "If it looks like a duck and behaves like a duck, it's a duck"

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()   # no type checking

make_sound(Dog())
make_sound(Cat())


# ==========================================================
# 2. OPERATOR OVERLOADING
# ==========================================================

# same operator behaves differently

print(2 + 3)        # integer addition
print("A" + "B")    # string concatenation

# custom operator overloading

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):   # overload +
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):   # string representation
        return f"({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2
print(p3)


# ==========================================================
# 3. METHOD OVERRIDING
# ==========================================================

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):   # overriding
        print("Dog barks")

a = Animal()
d = Dog()

a.sound()
d.sound()


# ==========================================================
# 4. METHOD OVERLOADING (SIMULATION)
# ==========================================================

# Python doesn't support directly → use default args

class Demo:
    def add(self, a, b, c=0):
        return a + b + c

obj = Demo()

print(obj.add(2, 3))
print(obj.add(2, 3, 4))


# ==========================================================
# BASE OVERRIDABLE METHODS (MAGIC METHODS)
# ==========================================================

class Example:

    def __init__(self, value):
        self.value = value
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

    def __repr__(self):
        return f"Example({self.value})"   # developer-friendly

    def __str__(self):
        return f"Value is {self.value}"   # user-friendly


obj = Example(10)

# __str__ is called
print(obj)

# __repr__ is called
print(repr(obj))

# delete object
del obj


# ==========================================================
# MORE OPERATOR OVERLOADING EXAMPLES
# ==========================================================

class Number:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __str__(self):
        return str(self.value)


n1 = Number(5)
n2 = Number(4)

print(n1 * n2)   # uses __mul__


# ==========================================================
# SUMMARY (IN COMMENTS)
# ==========================================================

# Polymorphism types:
#   1. Duck Typing
#   2. Operator Overloading
#   3. Method Overriding
#   4. Method Overloading (simulated)

# Magic methods:
#   __init__ → constructor
#   __del__ → destructor
#   __repr__ → developer representation
#   __str__ → user representation

# Benefit:
#   same interface, different behavior