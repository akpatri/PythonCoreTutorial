# ================================
# ITERABLES vs ITERATORS
# ================================

# Iterable:
# Any object that can return an iterator using __iter__()
# Examples: list, tuple, string, set, dict

my_list = [1, 2, 3]   # iterable

# Iterator:
# Object that produces items one at a time using __next__()
# Created from an iterable using iter()

my_iterator = iter(my_list)  # convert iterable → iterator

print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3
# print(next(my_iterator))  # Raises StopIteration


# ================================
# __iter__() and __next__()
# ================================

class SimpleIterator:
    def __init__(self):
        self.data = [10, 20, 30]
        self.index = 0

    def __iter__(self):
        # must return iterator object itself
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            # required to signal end of iteration
            raise StopIteration


obj = SimpleIterator()

for item in obj:   # internally uses __iter__() and __next__()
    print(item)


# ================================
# iter() FUNCTION
# ================================

# iter() converts iterable → iterator

numbers = [100, 200, 300]
it = iter(numbers)

print(next(it))  # 100


# iter() can also take a callable + sentinel
# keeps calling function until sentinel value is returned

def counter():
    counter.value += 1
    return counter.value

counter.value = 0

it = iter(counter, 5)

for i in it:
    print(i)  # prints 1, 2, 3, 4


# ================================
# ERROR HANDLING IN ITERATORS
# ================================

nums = [1, 2]
it = iter(nums)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("Iteration finished")
        break


# ================================
# CUSTOM ITERATOR
# ================================

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


cd = CountDown(5)

for num in cd:
    print(num)  # 5 4 3 2 1


# ================================
# GENERATOR (SIMPLER ITERATOR)
# ================================

# generator automatically implements iterator protocol

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # 1
print(next(gen))  # 2


# ================================
# ASYNCHRONOUS ITERATOR
# __aiter__() and __anext__()
# ================================

import asyncio

class AsyncCounter:
    def __init__(self, max_val):
        self.current = 0
        self.max_val = max_val

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.max_val:
            raise StopAsyncIteration

        await asyncio.sleep(1)  # simulate async work
        self.current += 1
        return self.current


async def main():
    async for value in AsyncCounter(3):
        print(value)  # prints 1, 2, 3 with delay


# run async loop
asyncio.run(main())


# ================================
# SUMMARY (IN COMMENTS)
# ================================

# Iterable:
#   has __iter__()
#   example: list, tuple

# Iterator:
#   has __iter__() + __next__()
#   returns values one by one

# iter(obj):
#   converts iterable → iterator

# next(obj):
#   gets next item or raises StopIteration

# Custom Iterator:
#   implement __iter__() and __next__()

# Generator:
#   uses yield, simpler way to create iterator

# Async Iterator:
#   uses __aiter__() and __anext__()
#   used with async for