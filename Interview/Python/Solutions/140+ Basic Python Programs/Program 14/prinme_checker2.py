# Author: Antim Pal
# date : 2025-04-19
# Problem: Write a program to check whether a number is prime or not.
# Approach: A prime number is a number that is only divisible by 1 and itself.

num = int(input("Enter a number: "))

# define a flag variable
flag = False
# prime number is equal to 1 or Less than 1
if num == 1:
     print(num,"is not a prime number")
# prime numbers are greater than 1
elif num > 1:
    # check for factors
    for i in range(2, num):
         if (num % i) == 0:
              # if a factor is found set flag to True
              flag = True 
              break
# if flag is True then number is not prime
if flag:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")
# Time Complexity: O(n)
# Space Complexity: O(1)
# The time complexity of this program is O(n) because in the worst case, we have to check all numbers from 2 to n-1 to determine if n is prime or not.
# The space complexity is O(1) because we are using a constant amount of space to store the flag variable and the input number.
# This program is not efficient for large numbers, as it checks all numbers from 2 to n-1 to determine if n is prime or not.