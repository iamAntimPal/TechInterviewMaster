# 🔍 Prime Number Checker (Python)

This Python program checks whether a given number is a **prime number**.

---

## 📌 Problem Statement

**Write a Python program to check if a number is a prime number.**

---

## 📚 What Are Prime Numbers?

A **prime number** is a whole number greater than 1 that **can only be divided** by 1 and itself, without leaving a remainder.

### ✅ Examples of Prime Numbers:
- 2, 3, 5, 7, 11, 13, 17, 19, 23...

### ❌ Not Prime:
- 1 is not a prime number.
- Any number divisible by numbers other than 1 and itself (e.g., 4, 6, 9, 15).

---

## ✅ Sample Code

```python
# Python program to check if a number is a prime number

# Input from user
num = int(input("Enter a number: "))

# Prime number check
if num <= 1:
    print(f"{num} is not a Prime Number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a Prime Number.")
    else:
        print(f"{num} is not a Prime Number.")
```

---

## ▶️ Example Runs

```bash
Enter a number: 7
7 is a Prime Number.
```

```bash
Enter a number: 12
12 is not a Prime Number.
```

```bash
Enter a number: 1
1 is not a Prime Number.
```

---

## 🚀 How to Run

1. Save the code in a file named `prime_checker.py`
2. Run the script using:

   ```bash
   python prime_checker.py
   ```

---

## 📁 Suggested Project Structure

```
prime_checker/
├── prime_checker.py
└── README.md
```

---

## 💡 You Can Try

- Display all prime numbers within a given range.
- Create a function `is_prime(n)` to reuse the logic.
- Visualize prime numbers on a number line using `matplotlib`.

---

Happy Coding! 🧠🔢
