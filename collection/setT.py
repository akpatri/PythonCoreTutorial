# setT.py
# Demonstration of Python Sets with examples and comments

# -------------------------------
# Creating a Set
# -------------------------------

# Using Curly Braces
set1 = {1, 2, 3, 4}
print("Set using {}:", set1)

# Using set() function
set2 = set([3, 4, 5, 6])
print("Set using set():", set2)


# -------------------------------
# Duplicate Elements in Set
# -------------------------------

dup_set = {1, 2, 2, 3, 3, 4}
print("Duplicates removed:", dup_set)


# -------------------------------
# Adding Elements
# -------------------------------

set1.add(10)  # Add single element
set1.update([20, 30])  # Add multiple elements
print("After adding elements:", set1)


# -------------------------------
# Removing Elements
# -------------------------------

set1.remove(10)   # Removes 10 (error if not found)
set1.discard(100) # No error if element not found

removed_item = set1.pop()  # Removes random element
print("Removed item using pop():", removed_item)
print("After removal:", set1)


# -------------------------------
# Membership Testing
# -------------------------------

print("Is 2 in set1?", 2 in set1)
print("Is 100 in set1?", 100 in set1)


# -------------------------------
# Set Operations
# -------------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print("Union:", A.union(B))      # Method
print("Union (|):", A | B)       # Operator

# Intersection
print("Intersection:", A.intersection(B))
print("Intersection (&):", A & B)

# Difference
print("Difference A-B:", A.difference(B))
print("Difference (-):", A - B)

# Symmetric Difference
print("Symmetric Difference:", A.symmetric_difference(B))
print("Symmetric (^):", A ^ B)


# -------------------------------
# Set Comprehensions
# -------------------------------

# Basic set comprehension
square_set = {x**2 for x in range(5)}
print("Square set:", square_set)

# Filtering elements
even_set = {x for x in range(10) if x % 2 == 0}
print("Even numbers:", even_set)

# Nested set comprehension
nested_set = {(x, y) for x in range(2) for y in range(2)}
print("Nested set:", nested_set)


# -------------------------------
# Frozen Sets (Immutable Sets)
# -------------------------------

frozen = frozenset([1, 2, 3, 4])
print("Frozen set:", frozen)

# frozen.add(5)  # ❌ Error: frozenset is immutable


# -------------------------------
# Access Set Items
# -------------------------------

my_set = {10, 20, 30, 40}

# Using for loop
print("Access using loop:")
for item in my_set:
    print(item)

# Using list comprehension
print("Access using list comprehension:")
print([item for item in my_set])


# -------------------------------
# Access Subset From a Set
# -------------------------------

A = {1, 2, 3, 4}
B = {2, 3}

print("Is B subset of A?", B.issubset(A))
print("Is A superset of B?", A.issuperset(B))


# -------------------------------
# Checking if Set Item Exists
# -------------------------------

if 3 in A:
    print("3 exists in set A")

if 10 not in A:
    print("10 does not exist in set A")