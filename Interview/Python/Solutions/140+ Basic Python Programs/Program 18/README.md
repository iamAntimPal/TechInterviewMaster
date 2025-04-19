# 🌀 Program 18: Fibonacci Sequence (Python)

This Python program prints the **Fibonacci sequence** up to a user-defined number of terms.

---

## 📌 Problem Statement

**Write a Python program to print the Fibonacci sequence.**

---

## 🔢 What is the Fibonacci Sequence?

The **Fibonacci sequence** is a series of numbers where each number is the sum of the two preceding ones, starting from **0** and **1**.

### 🔁 Sequence Pattern:
```

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

```

### 🧮 Mathematical Definition:

\[
F(0) = 0,\quad F(1) = 1,\quad F(n) = F(n-1) + F(n-2) \text{ for } n > 1
\]

---

## ✅ Sample Code

```python
# Python program to print the Fibonacci sequence up to n terms

# Input from user
n_terms = int(input("How many terms? "))

# First two terms
n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
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
        # Update values
        n1 = n2
        n2 = nth
        count += 1
```

---

## ▶️ Example Output

```bash
How many terms? 10
Fibonacci sequence up to 10 terms:
0 1 1 2 3 5 8 13 21 34
```

---

## 🚀 How to Run

1. Save the file as `fibonacci_sequence.py`
2. Run the program using:

   ```bash
   python fibonacci_sequence.py
   ```

---

## 📁 Suggested Project Structure

```
fibonacci_sequence/
├── fibonacci_sequence.py
└── README.md
```

---

## 💡 You Can Try

- Print Fibonacci numbers up to a specific **value** instead of **number of terms**.
- Implement Fibonacci using **recursion** or **dynamic programming**.
- Visualize the Fibonacci sequence using `matplotlib`.

---

Happy Coding! 🧠📈
