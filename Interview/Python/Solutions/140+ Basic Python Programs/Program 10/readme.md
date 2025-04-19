# 🔁 Swap Two Variables Without Temp (Python)

This Python program demonstrates how to **swap two variables without using a temporary variable**.

---

## 📌 Problem Statement

**Write a Python program to swap two variables without using a temporary variable.**

---

## 💡 Concept

Python allows variable swapping directly using tuple unpacking:

```python
a, b = b, a
```

This eliminates the need for a temporary variable.

---

## ✅ Sample Code

```python
# Python program to swap two variables without using a temporary variable

# Input from user
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print(f"Before swapping: a = {a}, b = {b}")

# Swapping without temp variable
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")
```

---

## ▶️ Example Run

```bash
Enter value of a: 5
Enter value of b: 10
Before swapping: a = 5, b = 10
After swapping: a = 10, b = 5
```

---

## 🚀 How to Run

1. Save the code in a file named `swap_variables.py`
2. Run the script:
   ```bash
   python swap_variables.py
   ```

---

## 📁 Suggested Project Structure

```
swap_variables/
├── swap_variables.py
└── README.md
```

---

## 💡 You Can Try

- Implement swapping using arithmetic operations (without tuple unpacking).
- Extend to swap values in a list or dictionary.
- Add type checking for inputs.

---

Happy Coding! 🔄🧠