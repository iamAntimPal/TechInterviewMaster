# 🔢 Prime Numbers in an Interval (Python)

This Python program prints all **prime numbers** in a given interval — in this case, from **1 to 10**.

---

## 📌 Problem Statement

**Write a Python program to print all prime numbers in an interval of 1-10.**

---

## 📚 What Are Prime Numbers?

A **prime number** is a natural number greater than 1 that has no positive divisors other than **1 and itself**.

### ✅ Prime numbers between 1 and 10:
- 2, 3, 5, 7

---

## ✅ Sample Code

```python
# Python program to print all prime numbers in an interval of 1 to 10

# Define the interval
start = 1
end = 10

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
```

---

## ▶️ Output

```bash
Prime numbers between 1 and 10 are:
2
3
5
7
```

---

## 🚀 How to Run

1. Save the code in a file named `primes_in_interval.py`
2. Run the script using:

   ```bash
   python primes_in_interval.py
   ```

---

## 📁 Suggested Project Structure

```
primes_in_interval/
├── primes_in_interval.py
└── README.md
```

---

## 💡 You Can Try

- Accept custom start and end points from user input.
- Count the total number of primes in the interval.
- Highlight twin primes (e.g., 3 & 5, 5 & 7).
- Visualize primes using plots or heatmaps.

---

Happy Coding! ✨🔍
