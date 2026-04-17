# ============================================
# LOOPS IN PYTHON
# ============================================

# --------------------------------------------
# 1. for LOOP
# --------------------------------------------

# used to iterate over iterable (list, tuple, string, etc.)

for i in range(5):
    print(i)   # prints 0 to 4


# loop through list

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# loop through string

for ch in "hello":
    print(ch)


# --------------------------------------------
# 2. while LOOP
# --------------------------------------------

# runs as long as condition is True

i = 0

while i < 5:
    print(i)
    i += 1   # increment


# infinite loop (use carefully)

# while True:
#     print("Running forever")


# --------------------------------------------
# 3. NESTED LOOPS
# --------------------------------------------

# loop inside another loop

for i in range(3):
    for j in range(2):
        print("i =", i, "j =", j)


# pattern example

for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()


# --------------------------------------------
# JUMP STATEMENTS IN LOOPS
# --------------------------------------------

# break, continue, pass


# --------------------------------------------
# 4. break
# --------------------------------------------

# exits the loop completely

for i in range(10):
    if i == 5:
        break
    print(i)   # prints 0 to 4


# break in while

i = 0
while True:
    if i == 3:
        break
    print(i)
    i += 1


# --------------------------------------------
# 5. continue
# --------------------------------------------

# skips current iteration

for i in range(5):
    if i == 2:
        continue
    print(i)   # skips 2


# continue in while

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


# --------------------------------------------
# 6. pass
# --------------------------------------------

# placeholder (does nothing)

for i in range(3):
    if i == 1:
        pass   # do nothing
    print(i)


# --------------------------------------------
# LOOP WITH else
# --------------------------------------------

# else runs when loop completes normally (no break)

for i in range(3):
    print(i)
else:
    print("Loop finished successfully")


# if break happens, else won't execute

for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This will NOT print")


# --------------------------------------------
# COMBINED EXAMPLE
# --------------------------------------------

for i in range(1, 6):
    if i == 2:
        continue   # skip 2
    if i == 5:
        break      # stop loop
    print("Value:", i)


# ============================================
# SUMMARY (IN COMMENTS)
# ============================================

# for loop:
#   iterate over sequence

# while loop:
#   runs based on condition

# nested loop:
#   loop inside loop

# break:
#   exit loop

# continue:
#   skip iteration

# pass:
#   do nothing (placeholder)

# else with loop:
#   executes if loop finishes without break