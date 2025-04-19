# Python program to swap two variables without using a temporary variable

# Input from user
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print(f"Before swapping: a = {a}, b = {b}")

# Swapping without temp variable
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")