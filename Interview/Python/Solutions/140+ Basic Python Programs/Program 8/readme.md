# 📅 Python Calendar Viewer

This Python program displays a **calendar** for a given month and year using Python's built-in `calendar` module.

---

## 📌 Problem Statement

**Write a Python program to display a calendar.**

---

## 📚 Module Used

- [`calendar`](https://docs.python.org/3/library/calendar.html): A built-in module that provides functions related to the calendar and date-related utilities.

---

## ✅ Sample Code

```python
# Python program to display a calendar

import calendar

# Input year and month from user
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Display calendar
print("\nHere is the calendar:")
print(calendar.month(year, month))
```

---

## ▶️ Example Run

```bash
Enter year: 2025
Enter month (1-12): 4

Here is the calendar:
     April 2025
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30
```

---

## 🚀 How to Run

1. Save the code in a file named `calendar_viewer.py`
2. Run the script using:
   ```bash
   python calendar_viewer.py
   ```

---

## 📁 Suggested Project Structure

```
calendar_viewer/
├── calendar_viewer.py
└── README.md
```

---

## 💡 You Can Try

- Display the full calendar for a whole year using `calendar.calendar(year)`.
- Add a GUI to let users pick a month/year.
- Highlight current day or weekends.
- Export calendar to a `.txt` file.

---

Happy Coding! 🗓️✨