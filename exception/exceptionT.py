# exceptionT.py

# -------------------------------
# BUILT-IN EXCEPTION (BASIC)
# -------------------------------

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


# -------------------------------
# try, except, else, finally
# -------------------------------

try:
    a = 10 / 2
except ZeroDivisionError:
    print("Error occurred")
else:
    print("No error:", a)     # runs if no exception
finally:
    print("Always executes") # runs always


# -------------------------------
# MULTIPLE EXCEPT CLAUSE
# -------------------------------

try:
    num = int("abc")
except (ValueError, TypeError):
    print("Handled multiple exceptions")


# -------------------------------
# EXCEPTION WITH ARGUMENT
# -------------------------------

try:
    raise ValueError("Invalid value")
except ValueError as e:
    print("Error message:", e)
    print("Args:", e.args)


# -------------------------------
# RAISE (MANUALLY THROW)
# -------------------------------

def check_age(age):
    if age < 18:
        raise Exception("Not eligible")

try:
    check_age(15)
except Exception as e:
    print(e)


# -------------------------------
# RAISE-IF PATTERN
# -------------------------------

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount

print(withdraw(1000, 500))


# -------------------------------
# USER-DEFINED EXCEPTION
# -------------------------------

class AgeError(Exception):

    def __init__(self, age, message="Invalid age"):
        self.age = age
        self.message = message
        super().__init__(self.message)   # initialize base class

    def __str__(self):
        return f"{self.message} → Age: {self.age}"


try:
    age = -5
    if age < 0:
        raise AgeError(age)
except AgeError as e:
    print(e)


# -------------------------------
# EXCEPTION CHAINING
# -------------------------------

try:
    try:
        int("abc")
    except ValueError as e:
        raise TypeError("Conversion failed") from e   # chaining
except TypeError as e:
    print("Chained:", e)


# -------------------------------
# NESTED TRY BLOCK
# -------------------------------

try:
    try:
        x = int("10")
        y = 10 / 0
    except ValueError:
        print("Inner ValueError")
    except ZeroDivisionError:
        print("Inner ZeroDivisionError")
finally:
    print("Outer finally always runs")


# -------------------------------
# CUSTOM MESSAGE + DEFAULT
# -------------------------------

try:
    raise AgeError(25, "Custom message")
except AgeError as e:
    print(e)


# -------------------------------
# FINALLY WITH RETURN
# -------------------------------

def test_finally():
    try:
        return "try block"
    finally:
        print("finally runs even after return")

print(test_finally())