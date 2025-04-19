a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
# Swapping without a temporary variable
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)
# Swapping using a temporary variable