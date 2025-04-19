# 💠 Program: Find Armstrong Numbers in an Interval (Python)

---

## 🧾 Problem Statement

**Write a Python Program to Find Armstrong Numbers in a Given Interval.**

---

## ❓ What is an Armstrong Number?

An **Armstrong number** (also known as a **narcissistic number**) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

---

### 🧮 Example:

- 153 is an Armstrong number because:  
  \[
  1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
  \]
- 9474 is an Armstrong number because:  
  \[
  9^4 + 4^4 + 7^4 + 4^4 = 9474
  \]

---

## ✅ Python Code

```python
# Python program to find Armstrong numbers in an interval

# Get interval input from user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print(f"\nArmstrong numbers between {lower} and {upper} are:")

# Loop through the interval
for num in range(lower, upper + 1):
    order = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)
```

---

## ▶️ Example Output

```
Enter lower range: 100
Enter upper range: 1000

Armstrong numbers between 100 and 1000 are:
153
370
371
407
```

---

## 📁 Suggested Project Structure

```
Program_ArmstrongInterval/
├── armstrong_interval.py
└── README.md
```

---

## 💡 You Can Try

- Check Armstrong numbers of higher digit ranges.
- Create a function and reuse it for single number or interval checking.
- Build a simple GUI using Tkinter for better interaction.

---

Happy Coding! 💻✨
