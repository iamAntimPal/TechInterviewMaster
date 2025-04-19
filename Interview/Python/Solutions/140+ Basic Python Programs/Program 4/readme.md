# 🔄 Swap Two Variables (Python)

This simple Python program demonstrates how to **swap the values of two variables** using different methods.

---

## 📌 Problem Statement

**Write a Python program to swap two variables.**

---

## 🧠 Concepts Covered

- Variable assignment
- Tuple unpacking (Pythonic way)
- Using a temporary variable

---

## 🧾 Sample Code

### ✅ Method 1: Using a Temporary Variable

```python
# Swapping using a temporary variable

x = input("Enter value for x: ")
y = input("Enter value for y: ")

# Swap logic
temp = x
x = y
y = temp

print("After swapping:")
print("x =", x)
print("y =", y)
```

---

### ✅ Method 2: Pythonic Way (Tuple Unpacking)

```python
# Swapping using tuple unpacking

x = input("Enter value for x: ")
y = input("Enter value for y: ")

x, y = y, x

print("After swapping:")
print("x =", x)
print("y =", y)
```

---

## ▶️ Example Run

```bash
Enter value for x: apple
Enter value for y: banana
After swapping:
x = banana
y = apple
```

---

## 🚀 How to Run

1. Save one of the examples in a `.py` file, e.g. `swap_variables.py`
2. Run the script:
   ```bash
   python swap_variables.py
   ```

---

## 📁 Suggested Project Structure

```
swap_variables/
├── swap_temp_variable.py
├── swap_tuple_unpacking.py
└── README.md
```

---

## 💡 You Can Try

- Swapping numbers instead of strings.
- Creating a reusable function.
- Adding unit tests to verify correct swapping.

---

# 📚 References
- [Python Tutorials](https://www.w3schools.com/python/)
- [Python Documentation](https://docs.python.org/3/tutorial/index.html)
- [Stack Overflow](https://stackoverflow.com/)
- [GeeksforGeeks](https://www.geeksforgeeks.org/)
- [Python for Data Analysis](https://www.oreilly.com/library/view/python-for-data/9781491957653/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Python Cookbook](https://www.oreilly.com/library/view/python-cookbook-3rd/9781449355735/)
## Happy Pythoning! 🐍✨