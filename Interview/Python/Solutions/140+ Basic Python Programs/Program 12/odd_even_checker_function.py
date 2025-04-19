# Solution:
# The program takes an integer input from the user and checks if it is odd or even using the modulus operator.

# using Funtion
def odd_even_checker(a):
     if a % 2 == 0:
          return "This number is Even number"
     else:
          return "This number is odd number"

a = int(input("Enter a number: "))
print(odd_even_checker(a))