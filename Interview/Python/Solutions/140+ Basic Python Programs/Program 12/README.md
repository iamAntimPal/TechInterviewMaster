# 🔢 Odd or Even Number Checker (Python)

This Python program checks whether a given number is **odd** or **even** using the modulo operator.

---

## 📌 Problem Statement

**Write a Python program to check if a number is odd or even.**

---

## ✅ Sample Code

```python
# Python program to check if the number is odd or even

# Input from user
num = int(input("Enter a number: "))

# Check and display result
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")
```

---

## ▶️ Example Runs

```bash
Enter a number: 8
8 is an Even number.
```

```bash
Enter a number: 7
7 is an Odd number.
```

---

## 🚀 How to Run

1. Save the code in a file named `odd_even_checker.py`
2. Run the script using:
   ```bash
   python odd_even_checker.py
   ```

---

## 📁 Suggested Project Structure

```
odd_even_checker/
├── odd_even_checker.py
└── README.md
```

---

## 💡 You Can Try

- Add input validation to handle non-integer inputs.
- Extend it to classify multiple numbers in a list.
- Create a GUI using `tkinter` for interactive input.

---

Happy Coding! ⚖️🔍
