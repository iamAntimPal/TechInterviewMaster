# 📐 Quadratic Equation Solver (Python)

This Python program solves **quadratic equations** of the form:

```
ax² + bx + c = 0
```

It uses the quadratic formula to compute the roots.

---

## 📌 Problem Statement

**Write a Python program to solve a quadratic equation.**

---

## 🧮 Quadratic Formula

```
x = (-b ± √(b² - 4ac)) / 2a
```

The value inside the square root, `b² - 4ac`, is called the **discriminant (D)**:
- If D > 0: Two real and distinct roots
- If D = 0: One real root (repeated)
- If D < 0: Two complex roots

---

## ✅ Sample Code

```python
import cmath  # For complex number support

# Get coefficients from user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Calculate the roots
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

# Display the result
print(f"The roots of the equation are {root1} and {root2}")
```

---

## ▶️ Example Run

```bash
Enter coefficient a: 1
Enter coefficient b: -3
Enter coefficient c: 2
The roots of the equation are (2+0j) and (1+0j)
```

---

## 🚀 How to Run

1. Save the code in a file named `quadratic_solver.py`
2. Run the script using:
   ```bash
   python quadratic_solver.py
   ```

---

## 📁 Suggested Project Structure

```
quadratic_solver/
├── quadratic_solver.py
└── README.md
```

---

## 💡 You Can Try

- Add input validation for `a != 0`.
- Format roots to hide the complex notation when not needed.
- Create a GUI using Tkinter.
- Add a plot of the quadratic curve using `matplotlib`.

---

Happy Solving! 🧮✨
