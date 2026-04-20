import mypackage

print("\n--- PACKAGE NAMESPACE ---")
print(dir(mypackage))  # shows what package exposes

print("\n--- ACCESSING VARIABLES ---")
print(mypackage.package_var)

print("\n--- USING EXPORTED FUNCTIONS ---")
print(mypackage.add(2, 3))
print(mypackage.name)

print("\n--- IMPORT * TEST ---")
from mypackage import *
print(add(5, 5))
print(name)

print("\n--- MODULE ACCESS ---")
import mypackage.math
print(mypackage.math.x)