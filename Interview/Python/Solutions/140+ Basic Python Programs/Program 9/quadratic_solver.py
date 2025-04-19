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