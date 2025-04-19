# ✖️ Multiplication Table Generator (Python)

This Python program generates and displays the **multiplication table** for a given number.

---

## 📌 Problem Statement

**Write a Python program to display the multiplication table of a number.**

---

## 🧮 What is a Multiplication Table?

A **multiplication table** lists the multiples of a number. For example, the multiplication table of 5 includes:  
`5 × 1 = 5`, `5 × 2 = 10`, `5 × 3 = 15`, ..., `5 × 10 = 50`.

---

## ✅ Sample Code

```python
# Python program to display the multiplication table

# Input from user
num = int(input("Enter a number to display its multiplication table: "))

# Display multiplication table from 1 to 10
print(f"\nMultiplication Table of {num}:\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

---

## ▶️ Example Output

```bash
Enter a number to display its multiplication table: 7

Multiplication Table of 7:

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

---

## 🚀 How to Run

1. Save the code in a file named `multiplication_table.py`
2. Run the script using:

   ```bash
   python multiplication_table.py
   ```

---

## 📁 Suggested Project Structure

```
multiplication_table/
├── multiplication_table.py
└── README.md
```

---

## 💡 You Can Try

- Let the user choose how far the table should go (e.g., 1 to 20).
- Display tables for a range of numbers (e.g., from 1 to 10).
- Format the output in a neat grid or table layout.

---

Happy Coding! 🧠✖️

