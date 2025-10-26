**Error handling** in programming means **detecting, managing, and responding to errors or exceptions** that occur while a program is running, instead of letting the program crash.

It helps make your programs **robust and user-friendly**.

---

### 🔹 In Python:

Python uses **exceptions** and `try-except` blocks to handle errors.

---

### 🔹 Syntax:

```python
try:
    # code that might raise an error
    result = 10 / 0
except ZeroDivisionError:
    # code to handle the error
    print("Cannot divide by zero!")
finally:
    # optional, code that runs always
    print("Execution completed.")
```

---

### 🔹 Output:

```
Cannot divide by zero!
Execution completed.
```

---

### 🔹 Key Points:

1. **`try`** → block of code where errors might occur.
2. **`except`** → block to handle specific or general errors.
3. **`finally`** → optional block, runs no matter what (good for cleanup).
4. **`else`** → optional, runs if no exception occurs.

---

### 🔹 Example: Multiple exceptions

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Invalid input, enter a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful")
finally:
    print("Program finished")
```

---

Would you like me to explain **the difference between compile-time and runtime errors** too?
