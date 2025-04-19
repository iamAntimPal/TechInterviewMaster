# ➕➖ Zero, Positive or Negative Number Checker (Python)

This Python program checks whether a given number is **positive**, **negative**, or **zero**.

---

## 📌 Problem Statement

**Write a Python program to check if a number is positive, negative, or zero.**

---

## ✅ Sample Code

```python
# Python program to check if the number is positive, negative or zero

# Input from user
num = float(input("Enter a number: "))

# Check and display result
if num > 0:
    print("The number is Positive.")
elif num == 0:
    print("The number is Zero.")
else:
    print("The number is Negative.")
```

---

## ▶️ Example Runs

```bash
Enter a number: 10
The number is Positive.
```

```bash
Enter a number: -5
The number is Negative.
```

```bash
Enter a number: 0
The number is Zero.
```

---

## 🚀 How to Run

1. Save the code in a file named `check_number.py`
2. Run the script:
   ```bash
   python check_number.py
   ```

---

## 📁 Suggested Project Structure

```
check_number/
├── check_number.py
└── README.md
```

---

## 💡 You Can Try

- Add input validation (e.g., reject non-numeric inputs).
- Extend the program to classify integers and floats separately.
- Create a GUI version using Tkinter.

---

Happy Coding! 🔍➕➖