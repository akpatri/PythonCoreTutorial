# ==========================================================
# DICTIONARIES IN PYTHON
# ==========================================================

# ==========================================================
# KEY FEATURES (IN COMMENTS)
# ==========================================================

# Unordered (before Python 3.7), now insertion order preserved
# Mutable (can modify)
# Indexed using keys (not numeric index)
# Unique keys
# Heterogeneous (any data types)


# ==========================================================
# CREATING A DICTIONARY
# ==========================================================

d = {"name": "Alice", "age": 25, "marks": 90}
print(d)

# using dict()
d2 = dict(a=1, b=2)
print(d2)


# ==========================================================
# ACCESSING DICTIONARY ITEMS
# ==========================================================

# using []
print(d["name"])

# using get()
print(d.get("age"))

# get with default
print(d.get("city", "Not Found"))


# ==========================================================
# ACCESS KEYS, VALUES, ITEMS
# ==========================================================

print(d.keys())    # keys
print(d.values())  # values
print(d.items())   # (key, value) pairs


# ==========================================================
# MODIFYING DICTIONARY
# ==========================================================

d["age"] = 30          # update existing
d["city"] = "Mysore"   # add new key
print(d)


# ==========================================================
# REMOVING ITEMS
# ==========================================================

del d["city"]          # delete by key

d.pop("age")           # remove and return value

d.popitem()            # removes last inserted item

print(d)


# ==========================================================
# ITERATING THROUGH DICTIONARY
# ==========================================================

# keys
for k in d:
    print(k)

# values
for v in d.values():
    print(v)

# key-value pairs
for k, v in d.items():
    print(k, v)


# ==========================================================
# PROPERTIES OF KEYS
# ==========================================================

# keys must be:
#   - unique
#   - immutable (int, string, tuple)

# example:
# d = {[1,2]: "value"}  # ERROR (list not allowed as key)


# ==========================================================
# DICTIONARY OPERATORS
# ==========================================================

d1 = {'a': 2, 'b': 4, 'c': 30}
d2 = {'a1': 20, 'b1': 40}

# access
print(d1['b'])

# assign
d1['b'] = 'Z'

# union (Python 3.9+)
d3 = d1 | d2
print(d3)

# update using |=
d1 |= d2
print(d1)


# ==========================================================
# DICTIONARY METHODS
# ==========================================================

d = {'x': 1, 'y': 2}

# copy
d_copy = d.copy()

# clear
d.clear()

# fromkeys
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)

# get
print(new_dict.get('a'))

# setdefault
new_dict.setdefault('d', 5)

# update
new_dict.update({'e': 10})

# keys, values, items
print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())


# ==========================================================
# BUILT-IN FUNCTIONS
# ==========================================================

d = {'a': 1, 'b': 2}

print(len(d))     # length
print(str(d))     # string
print(type(d))    # type


# ==========================================================
# ACCESS METHODS
# ==========================================================

# []
print(d['a'])

# get()
print(d.get('a'))

# values()
print(d.values())


# ==========================================================
# UPDATING MULTIPLE VALUES
# ==========================================================

d.update({'a': 100, 'b': 200})
print(d)


# ==========================================================
# CONDITIONAL MODIFICATION
# ==========================================================

if 'a' in d:
    d['a'] = 999


# ==========================================================
# ADDING NEW ITEMS
# ==========================================================

d['c'] = 300


# ==========================================================
# REMOVING ITEMS (MULTIPLE WAYS)
# ==========================================================

# del
del d['c']

# pop
d.pop('b')

# popitem
d.popitem()


# ==========================================================
# SUMMARY (IN COMMENTS)
# ==========================================================

# Dictionary:
#   key-value pairs

# Access:
#   d[key], d.get(key)

# Modify:
#   assign new value or add key

# Remove:
#   del, pop, popitem

# Iterate:
#   keys(), values(), items()

# Operators:
#   | , |= for merge

# Methods:
#   copy, clear, update, setdefault, fromkeys