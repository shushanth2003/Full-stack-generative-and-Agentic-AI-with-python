Perfect — this is a very core Python concept 👏

Let’s make it simple and clear:

---

### 🔹 **Class**

A **class** is a **blueprint** or **template** for creating objects.
It defines **how an object should behave** — what **attributes (data)** and **methods (actions)** it will have.

🧠 Example:

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand      # attribute
        self.color = color      # attribute
    
    def start(self):            # method
        print(f"{self.brand} is starting")
```

---

### 🔹 **Object**

An **object** is an **instance** (or real example) created from a class.
It has actual **values** for the attributes defined in the class.

🧠 Example:

```python
my_car = Car("BMW", "Black")
my_car.start()
```

**Output:**

```
BMW is starting
```

---

### 🔹 **Think Like This**

| Concept   | Meaning                                 | Example                        |
| --------- | --------------------------------------- | ------------------------------ |
| Class     | Blueprint                               | `Car`                          |
| Object    | Real-world example built from the class | `my_car = Car("BMW", "Black")` |
| Attribute | Data stored in object                   | `brand`, `color`               |
| Method    | Behavior or action                      | `start()`                      |

---

### 💡 Real-world analogy:

A **class** is like a **recipe** for making a cake 🍰
An **object** is the **actual cake** made using that recipe.

Excellent question 🔥 — you’re now moving into an **OOP advanced concept**.

Let’s break it down clearly 👇

---

### 🔹 What is **Attribute Shadowing** in Python?

**Attribute shadowing** happens when an **instance attribute** (created in the object) has the **same name** as a **class attribute**.
In that case, the **instance attribute “shadows” or hides** the class attribute.

That means when Python looks for the attribute,
👉 it first checks the **object’s (instance) namespace**,
👉 and only if not found, it checks the **class namespace**.

---

### 🔹 Example

```python
class Student:
    school = "ABC Public School"   # class attribute

# create object
s1 = Student()
print(s1.school)   # → ABC Public School (from class)

# shadowing
s1.school = "XYZ International School"
print(s1.school)   # → XYZ International School (instance attribute shadows class one)

# class attribute still unchanged
print(Student.school)  # → ABC Public School
```

---

### 🔹 What happened?

1. Initially, `s1.school` refers to the **class attribute**.
2. When we assign `s1.school = "XYZ..."`, we create a **new instance attribute** with the same name.
3. Now, `s1.school` points to the instance variable, **shadowing** the class variable.
4. But the **original class attribute** remains unchanged.

---

### 🔹 Quick Summary Table

| Attribute Type     | Scope                 | Accessed By                       | Can be Shadowed? |
| ------------------ | --------------------- | --------------------------------- | ---------------- |
| Class Attribute    | Shared by all objects | `ClassName.attr` or `object.attr` | ✅ Yes            |
| Instance Attribute | Unique per object     | `object.attr`                     | —                |

---


Good question 👏

In Python, **`__init__`** is the **constructor**.

---

### 🔹 Explanation

When you create an object:

```python
obj = MyClass()
```

Python automatically calls a **special method** named `__init__()`.

That’s why we say **`__init__` is the constructor in Python** —
it initializes the object’s attributes when the object is created.

---

### 🔹 Example

```python
class Car:
    def __init__(self, brand, color):   # constructor
        self.brand = brand
        self.color = color

my_car = Car("BMW", "Black")
print(my_car.brand)
```

**Output:**

```
BMW
```

---

### 🔹 Summary

| Language | Constructor Name           | Purpose                               |
| -------- | -------------------------- | ------------------------------------- |
| Java     | Class name (e.g., `Car()`) | Creates and initializes the object    |
| Python   | `__init__()`               | Initializes the object after creation |

---
In **Python**, you can access the **base (parent) class** using the **`super()`** function — just like Java’s `super` keyword.

---

### 🔹 Example: Accessing base class methods and variables

```python
class Animal:
    def __init__(self):
        self.type = "Mammal"

    def display_type(self):
        print("Type:", self.type)

class Dog(Animal):
    def __init__(self):
        super().__init__()   # calls Animal's constructor
        self.breed = "Labrador"

    def show(self):
        print("Breed:", self.breed)
        print("From Base Class:", super().type)  # access base class variable
        super().display_type()                   # call base class method

# main
dog = Dog()
dog.show()
```

---

### 🔹 Output:

```
Breed: Labrador
From Base Class: Mammal
Type: Mammal
```

---

### 🔹 Key Points:

1. `super().__init__()` → Calls the **constructor** of the base class.
2. `super().method()` → Calls a **method** from the base class.
3. You can also directly access base class members using the **class name**, like `Animal.display_type(self)`, but `super()` is preferred.

---
Excellent — your example is **perfect** for understanding the **MRO (Method Resolution Order)** in Python! 👏

Let’s go step by step.

---

### 🔹 What is MRO?

**MRO (Method Resolution Order)** defines **the order in which Python looks for methods or attributes** when you call them on an object in a class hierarchy (especially in **multiple inheritance**).

---

### 🔹 Your Code:

```python
class A:
    label = "Labeling class : A"

class B(A):
    label = "Labeling class : B"

class C(A):
    label = "Labeling class : C"

class D(B, C):
    label = "Labeling class : D"

cup = D()
print(cup.label)
print(D.__mro__)
```

---

### 🔹 Step-by-step execution:

1. **When you create `cup = D()`**, Python makes an object of class `D`.

2. **When you call `cup.label`**, Python checks where to find `label`.
   It searches classes in **MRO order** — **the sequence Python follows to find attributes and methods.**

---

### 🔹 The MRO of `D` is:

```python
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

That means:

```
D → B → C → A → object
```

---

### 🔹 So what happens when you call `cup.label`?

* Python looks in `D` first → finds `label = "Labeling class : D"` ✅
* So, it stops searching further.

Hence output:

```
Labeling class : D
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

---

### 🔹 Summary of MRO Rule:

Python uses the **C3 Linearization Algorithm** to determine MRO:

* It ensures a consistent and predictable search order.
* Child classes are checked **before** parent classes.
* The **leftmost base class** is checked first in multiple inheritance.

---




