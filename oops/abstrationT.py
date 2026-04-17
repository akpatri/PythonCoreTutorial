# ==========================================================
# PYTHON ABSTRACT CLASS
# ==========================================================

# Abstract classes are used to define a blueprint for other classes
# They cannot be instantiated directly

from abc import ABC, abstractmethod


# ==========================================================
# 1. CREATE AN ABSTRACT CLASS
# ==========================================================

class Animal(ABC):   # inherit from ABC

    # abstract method (must be implemented in child class)
    @abstractmethod
    def sound(self):
        pass


# a = Animal()  # ERROR: cannot instantiate abstract class


# ==========================================================
# 2. ABSTRACT METHOD (@abstractmethod)
# ==========================================================

# any class inheriting must implement this method

class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


d = Dog()
c = Cat()

d.sound()
c.sound()


# ==========================================================
# 3. ABSTRACT METHOD OVERRIDING
# ==========================================================

# child classes MUST override abstract methods

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):   # overriding abstract method
        return self.l * self.b


r = Rectangle(5, 4)
print(r.area())


# ==========================================================
# 4. CONCRETE METHOD (NORMAL METHOD IN ABSTRACT CLASS)
# ==========================================================

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    # concrete method (already implemented)
    def fuel_type(self):
        print("Uses fuel")


class Car(Vehicle):
    def start(self):
        print("Car starts with key")


car = Car()
car.start()       # abstract method implemented
car.fuel_type()   # inherited concrete method


# ==========================================================
# 5. MIX OF ABSTRACT + CONCRETE METHODS
# ==========================================================

class Bank(ABC):

    @abstractmethod
    def interest_rate(self):
        pass

    def display(self):
        print("Bank details")


class SBI(Bank):
    def interest_rate(self):
        print("Interest rate: 5%")


b = SBI()
b.interest_rate()
b.display()


# ==========================================================
# 6. MULTIPLE ABSTRACT METHODS
# ==========================================================

class Device(ABC):

    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass


class Laptop(Device):
    def power_on(self):
        print("Laptop ON")

    def power_off(self):
        print("Laptop OFF")


lap = Laptop()
lap.power_on()
lap.power_off()


# ==========================================================
# IMPORTANT NOTES (IN COMMENTS)
# ==========================================================

# Abstract Class:
#   - Created using ABC
#   - Cannot be instantiated

# @abstractmethod:
#   - Forces child class to implement method

# Abstract Method Overriding:
#   - Must override in subclass
#   - Otherwise subclass also becomes abstract

# Concrete Method:
#   - Normal method inside abstract class
#   - Can be directly used by child classes

# Key Rule:
#   If a class has at least one abstract method,
#   it cannot be instantiated