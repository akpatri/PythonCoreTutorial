# listT_full.py

# =========================================================
# 1. CREATING LIST
# =========================================================

# syntax:
# list_name = [item1, item2, ...]

lst = [1, 2, 3]
names = ["a", "b", "c"]


# =========================================================
# 2. ACCESSING VALUES IN LIST
# =========================================================

# syntax:
# list[index]

L = ['spam', 'Spam', 'SPAM!']

print(L[0])      # first element
print(L[-1])     # last element


# =========================================================
# 3. SLICING (SUBLIST)
# =========================================================

# syntax:
# list[start : end : step]

print(L[1:])     # from index 1 to end
print(L[:2])     # from start to index 2 (excluded)
print(L[::2])    # step
print(L[::-1])   # reverse


# =========================================================
# 4. UPDATING LIST
# =========================================================

# syntax:
# list[index] = new_value

lst = [1, 2, 3]
lst[0] = 100     # update single element

# syntax:
# list[start:end] = iterable

lst[1:3] = [20, 30]   # update multiple


# =========================================================
# 5. DELETING ELEMENTS
# =========================================================

# 1. del keyword
# syntax:
# del list[index]

lst = [1, 2, 3, 4]
del lst[1]

# 2. remove()
# syntax:
# list.remove(value)

lst.remove(3)

# 3. pop()
# syntax:
# list.pop(index)

lst.pop()        # last element
lst.pop(0)       # specific index

# 4. clear()
# syntax:
# list.clear()

lst.clear()


# =========================================================
# 6. LIST OPERATIONS
# =========================================================

# concatenation
# syntax: list1 + list2
print([1,2] + [3,4])

# repetition
# syntax: list * n
print(['Hi'] * 3)

# membership
# syntax: value in list
print(3 in [1,2,3])


# =========================================================
# 7. LIST METHODS (IMPORTANT)
# =========================================================

lst = [1, 2, 3]

# append()
# syntax: list.append(obj)
lst.append(4)

# extend()
# syntax: list.extend(iterable)
lst.extend([5,6])

# insert()
# syntax: list.insert(index, obj)
lst.insert(1, 100)

# remove()
# syntax: list.remove(obj)
lst.remove(100)

# pop()
# syntax: list.pop(index)
lst.pop()

# index()
# syntax: list.index(obj)
print(lst.index(2))

# count()
# syntax: list.count(obj)
print(lst.count(2))

# sort()
# syntax: list.sort()
lst.sort()

# reverse()
# syntax: list.reverse()
lst.reverse()

# copy()
# syntax: list.copy()
copy_lst = lst.copy()

# clear()
lst.clear()


# =========================================================
# 8. BUILT-IN FUNCTIONS
# =========================================================

lst = [10, 20, 5]

print(len(lst))     # length
print(max(lst))     # max
print(min(lst))     # min

# syntax:
# list(sequence)
print(list((1,2,3)))   # tuple → list


# =========================================================
# 9. LIST COMPREHENSION
# =========================================================

# syntax:
# new_list = [expression for item in iterable if condition]

# basic
nums = [x for x in range(5)]

# with condition
even = [x for x in range(10) if x % 2 == 0]

# with expression
squares = [x*x for x in range(5)]


# =========================================================
# 10. LIST COMPREHENSION WITH LAMBDA
# =========================================================

# syntax:
# map(lambda x: expression, iterable)

nums = [1,2,3]
result = list(map(lambda x: x*2, nums))


# =========================================================
# 11. NESTED LOOP IN LIST COMPREHENSION
# =========================================================

# syntax:
# [(x,y) for x in A for y in B]

pairs = [(x,y) for x in [1,2] for y in [3,4]]


# =========================================================
# 12. CONDITIONAL EXPRESSION
# =========================================================

# syntax:
# [value_if_true if condition else value_if_false for item in iterable]

nums = [1,2,3,4]
labels = ["even" if x%2==0 else "odd" for x in nums]


# =========================================================
# KEY NOTES
# =========================================================

# • Lists are MUTABLE (can change)
# • Ordered collection
# • Allows duplicate values
# • Supports indexing & slicing











