# genericT.py

# -------------------------------
# DEFINING A GENERIC FUNCTION
# -------------------------------

from typing import TypeVar

T = TypeVar('T')          # generic type

def show(value: T) -> T:
    return value         # works with any data type


# -------------------------------
# CALLING GENERIC FUNCTION
# -------------------------------

print(show(10))          # int
print(show(3.14))        # float
print(show("Python"))    # string
print(show([1, 2, 3]))   # list


# multiple generic types
T1 = TypeVar('T1')
T2 = TypeVar('T2')

def combine(a: T1, b: T2):
    return a, b          # returns tuple of different types

print(combine(10, "Hi"))     # (10, 'Hi')
print(combine(3.5, [1,2]))   # (3.5, [1,2])


# -------------------------------
# DEFINING A GENERIC CLASS
# -------------------------------

from typing import Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value

    def set(self, new_value: T):
        self.value = new_value


# -------------------------------
# USING GENERIC CLASS
# -------------------------------

int_box = Box
print(int_box.get())     # 10

str_box = Box[str]("Hello")
print(str_box.get())     # Hello

list_box = Box[list]([1,2,3])
print(list_box.get())    # [1, 2, 3]


# -------------------------------
# GENERIC CLASS WITH MULTIPLE TYPES
# -------------------------------

T1 = TypeVar('T1')
T2 = TypeVar('T2')

class Pair(Generic[T1, T2]):
    def __init__(self, first: T1, second: T2):
        self.first = first
        self.second = second

    def get_pair(self):
        return self.first, self.second


p1 = Pair[int, str](1, "One")
print(p1.get_pair())     # (1, 'One')

p2 = Pair[str, float]("Value", 2.5)
print(p2.get_pair())     # ('Value', 2.5)