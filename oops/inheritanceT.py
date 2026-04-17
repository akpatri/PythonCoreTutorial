# ==========================================================
# INHERITANCE IN PYTHON
# ==========================================================

# ==========================================================
# 1. CREATING A PARENT (BASE) CLASS
# ==========================================================

class Parent:
    def __init__(self):
        print("Parent constructor")

    def show(self):
        print("Parent method")


# ==========================================================
# 2. CREATING A CHILD (DERIVED) CLASS
# ==========================================================

class Child(Parent):   # inheritance
    def display(self):
        print("Child method")


c = Child()
c.show()      # inherited from Parent
c.display()   # own method


# ==========================================================
# TYPES OF INHERITANCE
# ==========================================================

# ----------------------------------------------------------
# 3. SINGLE INHERITANCE
# ----------------------------------------------------------

class A:
    def methodA(self):
        print("Class A")


class B(A):   # single inheritance
    def methodB(self):
        print("Class B")


obj = B()
obj.methodA()
obj.methodB()


# ----------------------------------------------------------
# 4. MULTIPLE INHERITANCE
# ----------------------------------------------------------

class X:
    def methodX(self):
        print("Class X")


class Y:
    def methodY(self):
        print("Class Y")


class Z(X, Y):   # inherits from multiple classes
    pass


z = Z()
z.methodX()
z.methodY()


# ----------------------------------------------------------
# 5. MULTILEVEL INHERITANCE
# ----------------------------------------------------------

class A1:
    def methodA1(self):
        print("Class A1")


class B1(A1):
    def methodB1(self):
        print("Class B1")


class C1(B1):
    def methodC1(self):
        print("Class C1")


c1 = C1()
c1.methodA1()
c1.methodB1()
c1.methodC1()


# ----------------------------------------------------------
# 6. HIERARCHICAL INHERITANCE
# ----------------------------------------------------------

class Parent2:
    def common(self):
        print("Common method")


class Child1(Parent2):
    pass


class Child2(Parent2):
    pass


obj1 = Child1()
obj2 = Child2()

obj1.common()
obj2.common()


# ----------------------------------------------------------
# 7. HYBRID INHERITANCE
# ----------------------------------------------------------

# combination of multiple + multilevel etc.

class A2:
    def showA(self):
        print("A2")


class B2(A2):
    def showB(self):
        print("B2")


class C2(A2):
    def showC(self):
        print("C2")


class D2(B2, C2):   # hybrid
    def showD(self):
        print("D2")


d = D2()
d.showA()
d.showB()
d.showC()
d.showD()


# ==========================================================
# 8. METHOD RESOLUTION ORDER (MRO)
# ==========================================================

# defines order in which base classes are searched

class M1:
    def show(self):
        print("M1")


class M2:
    def show(self):
        print("M2")


class M3(M1, M2):
    pass


m = M3()
m.show()   # follows MRO → M1 first

# check MRO
print(M3.__mro__)
# or
print(M3.mro())


# ==========================================================
# 9. super() FUNCTION
# ==========================================================

class Parent3:
    def __init__(self):
        print("Parent3 constructor")

    def display(self):
        print("Parent3 method")


class Child3(Parent3):
    def __init__(self):
        super().__init__()   # call parent constructor
        print("Child3 constructor")

    def display(self):
        super().display()    # call parent method
        print("Child3 method")


obj = Child3()
obj.display()


# ==========================================================
# METHOD OVERRIDING
# ==========================================================

class Base:
    def show(self):
        print("Base class method")


class Derived(Base):
    def show(self):   # overriding
        print("Derived class method")


d = Derived()
d.show()


# ==========================================================
# SUMMARY (IN COMMENTS)
# ==========================================================

# Parent Class:
#   base class

# Child Class:
#   inherits properties from parent

# Types:
#   Single → one parent
#   Multiple → multiple parents
#   Multilevel → chain inheritance
#   Hierarchical → one parent, many children
#   Hybrid → combination

# MRO:
#   order of searching methods
#   use Class.mro()

# super():
#   calls parent methods/constructors

# Method Overriding:
#   redefining parent method in child