# 📐 Triangle Area Calculator (Python)

This simple Python program calculates the **area of a triangle** using the basic mathematical formula.

---

## 📌 Problem Statement

**Write a Python program to find the area of a triangle.**

---

## 🧮 Formula Used

To find the area of a triangle when the base and height are known:

```
Area = (1/2) × base × height
```

---

## 🧑‍💻 Program Overview

The program:
- Prompts the user to enter the **base** and **height** of a triangle.
- Calculates the area using the formula.
- Displays the result with proper formatting.

---

## 🧾 Sample Code

```python
# Python program to find the area of a triangle

# Input from user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate area
area = 0.5 * base * height

# Display result
print("The area of the triangle is:", area)
```

---

## ▶️ Example Run

```bash
Enter the base of the triangle: 10
Enter the height of the triangle: 5
The area of the triangle is: 25.0
```

---

## 📦 How to Run

1. Save the code in a file named, for example, `triangle_area.py`
2. Run the program in a terminal:
   ```bash
   python triangle_area.py
   ```

---

## 💡 Enhancements You Can Try

- Add input validation (e.g., prevent negative or zero values).
- Create a function to calculate the area.
- Add support for Heron’s formula (when all 3 sides are known).

---

## 📁 Suggested Project Structure

```
triangle_area/
├── triangle_area.py
└── README.md
```

---

Happy Coding! 🎯
