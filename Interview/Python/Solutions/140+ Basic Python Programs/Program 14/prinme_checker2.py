# Author: Antim Pal
# date : 2025-04-19
# Problem: Write a program to check whether a number is prime or not.
# Approach: A prime number is a number that is only divisible by 1 and itself.

num = int(input("Enter a number: "))
# define a flag variable
flag = False
if num == 1:
 print(f"{num}, is not a prime number")
elif num > 1:
 # check for factors
 for i in range(2, num):
 if (num % i) == 0:
 flag = True # if factor is found, set flag to True
 # break out of loop
 break
 # check if flag is True
if flag:
 print(f"{num}, is not a prime number")
else:
 print(f"{num}, is a prime number")