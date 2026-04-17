# ==========================================================
# ARRAY REPRESENTATION IN PYTHON
# ==========================================================

# Python arrays are provided by the "array" module
# Unlike lists, arrays store elements of SAME data type

from array import array


# ==========================================================
# CREATING ARRAY
# ==========================================================

# syntax: array(typecode, initializer)

# typecode → defines data type
# initializer → iterable (list, tuple, etc.)

arr = array('i', [1, 2, 3, 4])  # 'i' → signed integer
print(arr)


# ==========================================================
# TYPECODE EXAMPLES
# ==========================================================

# 'i' → integer
# 'f' → float
# 'd' → double
# 'b' → signed int (1 byte)

arr_float = array('f', [1.1, 2.2, 3.3])
print(arr_float)


# ==========================================================
# ACCESSING ARRAY ELEMENTS
# ==========================================================

# using indexing
print(arr[0])   # first element

# using iteration
for i in arr:
    print(i)

# using enumerate()
for index, value in enumerate(arr):
    print(index, value)


# ==========================================================
# SLICING (ACCESS RANGE)
# ==========================================================

print(arr[:2])     # from start to index 2
print(arr[1:3])    # index 1 to 2
print(arr[2:])     # from index 2 to end
print(arr[::-1])   # reverse


# ==========================================================
# BASIC OPERATIONS
# ==========================================================

# Traverse
for x in arr:
    print(x)

# Insertion
arr.insert(1, 99)
print(arr)

# Deletion
arr.remove(99)
print(arr)

# Search
print(arr.index(3))   # index of value

# Update
arr[0] = 100
print(arr)


# ==========================================================
# ADDING ELEMENTS
# ==========================================================

arr.append(10)              # add at end
arr.extend([20, 30])        # add multiple
arr.insert(1, 5)            # insert at index
print(arr)


# ==========================================================
# REMOVING ELEMENTS
# ==========================================================

arr.remove(5)   # remove first occurrence
arr.pop()       # remove last element
arr.pop(0)      # remove by index
print(arr)


# ==========================================================
# LOOPING
# ==========================================================

# for loop
for x in arr:
    print(x)

# while loop
i = 0
while i < len(arr):
    print(arr[i])
    i += 1

# with index
for i in range(len(arr)):
    print(i, arr[i])


# ==========================================================
# COPYING ARRAYS
# ==========================================================

# shallow copy (assignment)
arr2 = arr

# deep copy
import copy
arr3 = copy.deepcopy(arr)


# ==========================================================
# REVERSING ARRAY
# ==========================================================

# slicing
rev = arr[::-1]

# reverse() method
arr.reverse()

# reversed()
rev2 = list(reversed(arr))


# ==========================================================
# JOIN ARRAYS
# ==========================================================

a1 = array('i', [1, 2])
a2 = array('i', [3, 4])

# using extend
a1.extend(a2)

# using + (convert to list)
a3 = array('i', list(a1) + list(a2))


# ==========================================================
# INFORMATION & UTILITY METHODS
# ==========================================================

print(arr.buffer_info())   # (address, length)
print(arr.count(2))        # count occurrences
print(arr.index(3))        # find index


# ==========================================================
# MANIPULATING METHODS
# ==========================================================

arr.reverse()   # reverse array

# byteswap (system-dependent use)
arr.byteswap()


# ==========================================================
# CONVERSION METHODS
# ==========================================================

# to list
lst = arr.tolist()

# from list
arr.fromlist([7, 8, 9])

# to bytes
b = arr.tobytes()

# from bytes
arr.frombytes(b)