# 📆 Leap Year Checker (Python)

This Python program checks whether a given year is a **leap year** or not, following the rules defined by the Gregorian calendar.

---

## 📌 Problem Statement

**Write a Python program to check if a year is a leap year.**

---

## 🔢 What is a Leap Year?

A year is a leap year if:
- It is divisible by 4 **and**
  - Not divisible by 100 **unless** also divisible by 400.

### ✅ Leap Year Rules:
- ✅ 2000 → Leap Year (divisible by 400)
- ❌ 1900 → Not a Leap Year (divisible by 100 but not 400)
- ✅ 2024 → Leap Year (divisible by 4 and not 100)

---

## ✅ Sample Code

```python
# Python program to check if a year is a leap year

# Input from user
year = int(input("Enter a year: "))

# Check leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is Not a Leap Year.")
```

---

## ▶️ Example Runs

```bash
Enter a year: 2024
2024 is a Leap Year.
```

```bash
Enter a year: 1900
1900 is Not a Leap Year.
```

```bash
Enter a year: 2000
2000 is a Leap Year.
```

---

## 🚀 How to Run

1. Save the code in a file named `leap_year_checker.py`
2. Run the script using:

   ```bash
   python leap_year_checker.py
   ```

---

## 📁 Suggested Project Structure

```
leap_year_checker/
├── leap_year_checker.py
└── README.md
```

---

## 💡 You Can Try

- Check leap years in a given range.
- Create a GUI calendar widget that highlights leap years.
- Save results to a text file or CSV.

---

Happy Coding! 🌟📅
