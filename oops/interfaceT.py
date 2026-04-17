# ==========================================================
# INTERFACES IN PYTHON
# ==========================================================

# Python does not have a built-in "interface" keyword like Java
# But we can implement interfaces in two ways:
#   1. Formal Interface (using ABC)
#   2. Informal Interface (duck typing)


# ==========================================================
# 1. FORMAL INTERFACE (USING ABSTRACT BASE CLASS)
# ==========================================================

from abc import ABC, abstractmethod

# defining interface
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# implementing interface
class Rectangle(Shape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)


r = Rectangle(5, 3)
print(r.area())
print(r.perimeter())


# class must implement ALL abstract methods

# class Incomplete(Shape):
#     def area(self):
#         return 0
#     # missing perimeter()
# → This will make class abstract and cannot be instantiated


# obj = Incomplete()  # ERROR


# ==========================================================
# 2. INFORMAL INTERFACE (DUCK TYPING)
# ==========================================================

# No inheritance required
# Just implement required methods

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

# function expecting "interface-like" behavior

def make_sound(animal):
    animal.speak()   # works if method exists


d = Dog()
c = Cat()

make_sound(d)
make_sound(c)


# ==========================================================
# RULES FOR INTERFACES (IN COMMENTS)
# ==========================================================

# 1. Methods inside interface must be abstract
#    → use @abstractmethod

# 2. Cannot create object of interface
#    → Shape() not allowed

# 3. Child class must implement ALL methods
#    → otherwise it becomes abstract

# 4. If not all methods implemented:
#    → class must also inherit ABC and remain abstract


# ==========================================================
# PARTIAL IMPLEMENTATION (ABSTRACT CLASS)
# ==========================================================

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def fuel(self):   # concrete method allowed
        print("Uses fuel")


class Car(Vehicle):
    def start(self):
        print("Car starts")


car = Car()
car.start()
car.fuel()


# ==========================================================
# MULTIPLE INTERFACES
# ==========================================================

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Duck(Flyable, Swimmable):
    def fly(self):
        print("Duck flies")

    def swim(self):
        print("Duck swims")


d = Duck()
d.fly()
d.swim()


# ==========================================================
# SUMMARY (IN COMMENTS)
# ==========================================================

# Formal Interface:
#   uses ABC + @abstractmethod
#   strict implementation

# Informal Interface:
#   duck typing
#   "if it behaves like interface, it's accepted"

# Key Rules:
#   - cannot instantiate interface
#   - must implement all abstract methods
#   - else class becomes abstract