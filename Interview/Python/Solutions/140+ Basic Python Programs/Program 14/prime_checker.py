# Program to check if a number is prime or not 
# A prime number is a number that is only divisible by 1 and itself
# For example 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97 are prime numbers

# To take input from the user 
num = int(input("enter a number:"))
# To check if the number is prime or not 
if num > 1:
     for i in range(2,num):
          if (num % i) == 0:
               # If the number is divisible by any number between 2 and num-1, it is not prime 
               print(num, "is not a prime number")
               break
          else:
               print(num, "is a prime numnber")
               break
