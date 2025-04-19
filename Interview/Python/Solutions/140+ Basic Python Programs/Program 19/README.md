# 📘 Program 18: Python Program to Print the Fibonacci Sequence

---

## 🧾 Problem Statement

**Write a Python Program to Print the Fibonacci Sequence.**

---

## 📚 Description

The **Fibonacci sequence** is a series of numbers where each number is the sum of the two preceding ones. It starts with 0 and 1, and the next number in the sequence is obtained by adding the two previous numbers.

---

### 📌 Fibonacci Sequence Example:
```

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

```

---

### 🧮 Mathematical Representation:

The Fibonacci sequence can be defined by the recurrence relation:

\[
F(0) = 0, \quad F(1) = 1, \quad F(n) = F(n - 1) + F(n - 2) \text{ for } n > 1
\]

---

## ✅ Python Code

```python
# Python Program to Print the Fibonacci Sequence

# Take input from user
n_terms = int(input("How many terms? "))

# First two Fibonacci numbers
n1, n2 = 0, 1
count = 0

# Check if the number is valid
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence up to 1 term:")
    print(n1)
else:
    print(f"Fibonacci sequence up to {n_terms} terms:")
    while count < n_terms:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
```

---

## ▶️ Example Output

```
How many terms? 10
Fibonacci sequence up to 10 terms:
0 1 1 2 3 5 8 13 21 34
```

---

## 💡 Additional Ideas

- Implement using **recursion** or **memoization**.
- Visualize Fibonacci numbers with `matplotlib`.
- Print Fibonacci numbers **up to a given maximum value**, not just by count.

---

## 📂 Suggested Structure

```
Program18_FibonacciSequence/
├── fibonacci.py
└── README.md
```

---

Happy Learning! 🚀
