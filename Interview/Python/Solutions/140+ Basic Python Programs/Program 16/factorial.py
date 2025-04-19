# Factorial of a number using recursion
def factorial(n):
     if n == 1:
          return 1
     elif n == 0:
          return 0
     else:
          return n * factorial(n-1)
num = int(input("Enter a number: "))
print("The factorial of", num, "is", factorial(num))