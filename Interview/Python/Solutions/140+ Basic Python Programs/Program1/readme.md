# 🐍 Hello World Printer (10 Times)

This simple Python program demonstrates multiple ways to print **"Hello World"** ten times using different approaches like `print()` statements, loops, and functions.

## 🧠 Problem Statement

Write a Python program to print `"Hello World"` 10 times.

---

## ✅ Solutions Included

### 🔹 Solution 1: Using `print()` Manually
Print `"Hello World"` multiple times by repeating the `print()` statement.

```python
print("Hello World")
print("Hello World")
# (repeat 10 times manually)
```

---

### 🔹 Solution 2: Using a `for` Loop
Leverage a `for` loop to print it 10 times efficiently.

```python
for i in range(10):
    print("Hello World")
```

---

### 🔹 Solution 3: Using a Function with Loop
Encapsulate the loop logic in a function to make it reusable.

```python
def print_hello_world(n):
    """
    This function prints "Hello World" n times.
    """
    for _ in range(n):
        print("Hello World")

print_hello_world(10)
```

---

### 🔹 Solution 4: Return-Based Function (for learning purposes)
Demonstrates a function that returns the string instead of printing it directly.

```python
def hello_world():
    """
    This function returns the string "Hello World".
    """
    return "Hello World"

print(hello_world())
```

> ⚠️ Note: This version only prints "Hello World" once. To print 10 times, you need to loop the `print(hello_world())` call.

---

## 🚀 How to Run

1. Save any of the solutions in a `.py` file, for example:
   ```bash
   hello_world.py
   ```

2. Run the script using:
   ```bash
   python hello_world.py
   ```

---

## 🛠 Recommended Improvements

- Add user input to customize how many times it prints.
- Add error handling for non-integer input.
- Explore list comprehensions (for learning, not readability).

---

## 📁 Repository Structure Suggestion

```
hello_world_10_times/
├── solution1_manual_print.py
├── solution2_for_loop.py
├── solution3_function_loop.py
├── solution4_function_return.py
└── README.md
```

---

## ✍️ Author

This is a beginner-friendly project ideal for Python learners. Contributions and variations are welcome!

---

Happy Coding! 🎉

<p align="right">
<a href="./../Program2/readme.md">Next Program</a>
</p>