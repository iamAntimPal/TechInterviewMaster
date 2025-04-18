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