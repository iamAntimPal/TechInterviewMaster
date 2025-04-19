# ✨ Factorial Calculator (Python)

This Python program calculates the **factorial** of a given non-negative integer using a `for` loop.

---

## 📌 Problem Statement

**Write a Python program to find the factorial of a number.**

---

## ℹ️ What is a Factorial?

The **factorial** of a number `n` (written as `n!`) is the product of all positive integers from `1` to `n`.

### ✅ Examples:

- `5! = 5 × 4 × 3 × 2 × 1 = 120`
- `0! = 1` (by definition)

---

## ✅ Sample Code

```python
# Python program to find the factorial of a number

# Input from user
num = int(input("Enter a non-negative integer: "))

# Factorial calculation
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
```

---

## ▶️ Example Runs

```bash
Enter a non-negative integer: 5
The factorial of 5 is 120
```

```bash
Enter a non-negative integer: 0
The factorial of 0 is 1
```

```bash
Enter a non-negative integer: -3
Factorial is not defined for negative numbers.
```

---

## 🚀 How to Run

1. Save the code in a file named `factorial.py`
2. Run the script using:

   ```bash
   python factorial.py
   ```

---

## 📁 Suggested Project Structure

```
factorial/
├── factorial.py
└── README.md
```

---

## 💡 You Can Try

- Implement the factorial using **recursion**.
- Use the built-in `math.factorial()` function for comparison.
- Plot the growth of factorial values using `matplotlib`.

---

Happy Coding! 🔢🎯

