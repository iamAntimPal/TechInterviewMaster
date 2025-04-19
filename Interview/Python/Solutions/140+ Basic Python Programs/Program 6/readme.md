 🛣️ Kilometers to Miles Converter (Python)

This Python program allows users to convert distances from **kilometers to miles** using a standard mathematical formula.

---

## 📌 Problem Statement

**Write a Python program to convert kilometers to miles.**

---

## 🧮 Conversion Formula

```
1 kilometer = 0.621371 miles
```

To convert kilometers to miles:
```
miles = kilometers × 0.621371
```

---

## ✅ Sample Code

```python
# Python program to convert kilometers to miles

# Input from user
kilometers = float(input("Enter distance in kilometers: "))

# Conversion factor
conversion_factor = 0.621371

# Calculate miles
miles = kilometers * conversion_factor

# Display result
print(f"{kilometers} kilometers is equal to {miles:.2f} miles")
```

---

## ▶️ Example Run

```bash
Enter distance in kilometers: 10
10.0 kilometers is equal to 6.21 miles
```

---

## 🚀 How to Run

1. Save the code in a file named `km_to_miles.py`
2. Run the script in your terminal:
   ```bash
   python km_to_miles.py
   ```

---

## 📁 Suggested Project Structure

```
km_to_miles_converter/
├── km_to_miles.py
└── README.md
```

---

## 💡 You Can Try

- Add miles to kilometers conversion (bi-directional).
- Build a simple GUI using Tkinter.
- Accept command-line arguments instead of interactive input.
- Add unit tests for conversion logic.

---

Happy Coding! 🌍🚗
