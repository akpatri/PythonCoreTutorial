# ==========================================================
# CREATING CLASSES IN PYTHON
# ==========================================================

class Student:
    """This is a Student class (Docstring example)"""

    # class attribute
    school = "ABC School"

    def __init__(self, name, marks):
        # instance attributes
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)


# accessing docstring
print(Student.__doc__)


# ==========================================================
# ACCESSING ATTRIBUTES USING BUILT-IN FUNCTIONS
# ==========================================================

s = Student("John", 90)

print(getattr(s, "name"))           # get attribute
print(hasattr(s, "marks"))         # check attribute
setattr(s, "age", 20)              # set new attribute
print(s.age)

delattr(s, "age")                  # delete attribute


# ==========================================================
# BUILT-IN CLASS ATTRIBUTES
# ==========================================================

print(Student.__dict__)    # namespace dictionary
print(Student.__name__)    # class name
print(Student.__module__)  # module name
print(Student.__bases__)   # base classes


# ==========================================================
# INSTANCE vs CLASS ATTRIBUTES
# ==========================================================

class Demo:
    class_var = 100   # class attribute

    def __init__(self):
        self.inst_var = 10   # instance attribute


d1 = Demo()
d2 = Demo()

d1.inst_var = 50   # affects only d1
Demo.class_var = 200  # affects all objects

print(d1.inst_var, d2.inst_var)
print(d1.class_var, d2.class_var)


# ==========================================================
# CLASS METHODS
# ==========================================================

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def show_count(cls):
        print(cls.count)


obj1 = MyClass()
obj2 = MyClass()
MyClass.show_count()


# using classmethod() function

def display(cls):
    print("Class name:", cls.__name__)

MyClass.show = classmethod(display)
MyClass.show()


# dynamically delete class method
del MyClass.show


# ==========================================================
# STATIC METHODS
# ==========================================================

class Math:

    @staticmethod
    def add(a, b):
        return a + b


print(Math.add(2, 3))

# using staticmethod() function
def sub(a, b):
    return a - b

Math.sub = staticmethod(sub)
print(Math.sub(5, 2))


# ==========================================================
# CONSTRUCTORS
# ==========================================================

# default constructor

class A:
    def __init__(self):
        print("Default constructor")


# parameterized constructor

class B:
    def __init__(self, x):
        self.x = x


# ==========================================================
# ACCESS MODIFIERS (CONVENTION BASED)
# ==========================================================

class Test:
    def __init__(self):
        self.public = 1        # public
        self._protected = 2    # protected (convention)
        self.__private = 3     # private (name mangling)

t = Test()
print(t.public)
print(t._protected)
# print(t.__private)  # error

# accessing private (name mangling)
print(t._Test__private)


# ==========================================================
# PROPERTY (ENCAPSULATION)
# ==========================================================

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name)


p = Person("Alice")
print(p.name)
p.name = "Bob"
print(p.name)


# ==========================================================
# INNER CLASS
# ==========================================================

class Outer:
    class Inner:
        def show(self):
            print("Inner class method")


o = Outer()
i = Outer.Inner()
i.show()


# ==========================================================
# ANONYMOUS CLASS USING type()
# ==========================================================

NewClass = type("NewClass", (), {"x": 10, "show": lambda self: print(self.x)})

obj = NewClass()
obj.show()


# ==========================================================
# SINGLETON CLASS
# ==========================================================

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


a = Singleton()
b = Singleton()

print(a is b)  # True (same instance)


# ==========================================================
# DATACLASS
# ==========================================================

from dataclasses import dataclass, field, asdict

@dataclass
class Product:
    name: str
    price: int
    qty: int = 0   # default value


p1 = Product("Pen", 10, 5)
print(p1)

# convert to dictionary
print(asdict(p1))


# mutable default example

@dataclass
class Basket:
    items: list = field(default_factory=list)


b = Basket()
b.items.append("apple")
print(b.items)


# frozen (immutable)

@dataclass(frozen=True)
class Point:
    x: int
    y: int


pt = Point(1, 2)
# pt.x = 10  # error (immutable)


# post init

@dataclass
class Order:
    price: int
    qty: int
    total: int = 0

    def __post_init__(self):
        self.total = self.price * self.qty


o = Order(10, 5)
print(o.total)


# ==========================================================
# __str__ and __repr__
# ==========================================================

class Example:
    def __str__(self):
        return "User-friendly string"

    def __repr__(self):
        return "Developer representation"


e = Example()
print(str(e))
print(repr(e))