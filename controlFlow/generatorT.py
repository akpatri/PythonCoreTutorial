# ============================================
# GENERATORS IN PYTHON
# ============================================

# A generator is a special type of iterator
# It generates values one at a time using "yield"


# ============================================
# 1. GENERATOR FUNCTION
# ============================================

# A function that uses "yield" instead of "return"

def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

# __next__() is used internally by next()
print(gen.__next__())  # 1
print(next(gen))       # 2
print(next(gen))       # 3
# print(next(gen))     # StopIteration


# ============================================
# HOW GENERATOR WORKS (STATE SAVING)
# ============================================

def demo():
    print("Start")
    yield 10
    print("Middle")
    yield 20
    print("End")

g = demo()

print(next(g))  # Start → 10
print(next(g))  # Middle → 20
# next(g)       # End → StopIteration


# ============================================
# 2. GENERATOR EXPRESSIONS
# ============================================

# Similar to list comprehension but uses ()
# NOTE: correct syntax uses parentheses (), NOT {}

gen_expr = (x * x for x in range(5))

print(next(gen_expr))  # 0
print(next(gen_expr))  # 1

for val in gen_expr:
    print(val)  # remaining values


# Comparison with list (memory heavy)
list_comp = [x * x for x in range(5)]   # creates full list in memory
gen_expr = (x * x for x in range(5))    # lazy evaluation (one by one)


# ============================================
# GENERATOR EXPRESSION SYNTAX
# ============================================

# (expression for item in iterable if condition)

gen_expr = (x for x in range(10) if x % 2 == 0)

for num in gen_expr:
    print(num)  # even numbers


# ============================================
# EXCEPTION HANDLING IN GENERATORS
# ============================================

def safe_generator():
    yield 1
    yield 2
    raise ValueError("Something went wrong!")
    yield 3  # never reached

g = safe_generator()

try:
    while True:
        print(next(g))
except StopIteration:
    print("Finished normally")
except Exception as e:
    print("Exception occurred:", e)


# Handling inside generator

def handled_generator():
    try:
        yield 1
        yield 2
        raise ValueError("Error inside generator")
    except ValueError as e:
        print("Handled:", e)
    yield 3

g = handled_generator()

for val in g:
    print(val)


# ============================================
# GENERATOR FUNCTION (REAL EXAMPLE)
# ============================================

# Infinite generator

def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1

counter = infinite_counter()

print(next(counter))  # 0
print(next(counter))  # 1


# ============================================
# ASYNCHRONOUS GENERATOR
# ============================================

import asyncio

# syntax:
# async def generator():
#     yield value

async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)  # simulate async work
        yield i


async def main():
    gen = async_generator()

    # using anext()
    print(await anext(gen))  # 0

    # using async for
    async for value in gen:
        print(value)  # 1, 2


asyncio.run(main())


# ============================================
# MANUAL USE OF __anext__()
# ============================================

async def manual_async():
    gen = async_generator()

    try:
        while True:
            val = await gen.__anext__()
            print(val)
    except StopAsyncIteration:
        print("Async iteration finished")

asyncio.run(manual_async())


# ============================================
# GENERATOR vs NORMAL FUNCTION
# ============================================

def normal_function():
    return [1, 2, 3]  # returns all at once

def generator_function():
    yield 1
    yield 2
    yield 3  # returns one by one


# ============================================
# KEY POINTS (IN COMMENTS)
# ============================================

# Generator Function:
#   uses "yield"
#   maintains state between calls

# Generator Expression:
#   (expression for item in iterable)
#   memory efficient

# __next__():
#   retrieves next value
#   raises StopIteration when done

# Exception Handling:
#   can handle inside or outside generator

# Async Generator:
#   uses async def + yield
#   uses async for or anext()

# Advantage:
#   saves memory (lazy evaluation)
#   useful for large datasets / streams