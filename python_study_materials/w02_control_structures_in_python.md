# **Week 02: Control Structures in Python**

---

### Slide 01: Overview

* **Topic**: Control Structures
* **Focus**: Making decisions and repeating tasks in code
* **Objective**: Learn to use `if`, `else`, `elif`, and loops (`for`, `while`)

---

### Slide 02: Why Control Structures Matter

* Allow decision-making in code
* Help automate repetitive tasks
* Essential for real-world problem solving (e.g., design logic, conditional formulas)

---

### Slide 03: `if` Statement

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

* Executes a block if the condition is True

---

### Slide 04: `if-else` Statement

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
```

* Choose between two options

---

### Slide 05: `elif` Statement

```python
x = 5
if x > 5:
    print("Greater")
elif x == 5:
    print("Equal")
else:
    print("Less")
```

* Use when there are multiple conditions to check

---

### Slide 06: Logical Operators

* Combine conditions using:

  * `and`
  * `or`
  * `not`

```python
age = 25
if age > 18 and age < 60:
    print("Working age")
```

---

### Slide 07: `while` Loop

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

* Repeats as long as condition is True

---

### Slide 08: `for` Loop

```python
for i in range(1, 6):
    print(i)
```

* Iterates over a sequence or range

---

### Slide 09: `break` and `continue`

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

* `break`: exits the loop
* `continue`: skips current iteration

---

### Slide 10: Practical Example - Grading System

```python
marks = 85
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
else:
    print("Below A")
```

* Real-world decision-making logic

---

### Slide 11: Lab Tasks

* Write programs using `if`, `elif`, and `else`
* Use loops to print number patterns or sequences
* Create simple logic like a basic calculator or grading system

---

### Slide 12: Summary

* `if`, `else`, and `elif` control the program flow
* `for` and `while` help repeat tasks
* `break` and `continue` give you more control in loops

---

### Slide 13: Q\&A?

* Any questions?
