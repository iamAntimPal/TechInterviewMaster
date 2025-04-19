# Author: Antim Pal
# Date: 20-04-2025
# Description: Multiplication table in Python

# Multiplication table
# Program to create a multiplication 
# A multiplication table (from 1 to 10) in Python
# using for loop
# using while loop
# using list comprehension
# Solution:
# 1. Using for loop
# 2. Using while loop
# 3. Using list comprehension

# Using for loop
num = int(input("Enter the number to create a multiplication table for:"))
print(f"Multiplication table of {num} using for loop:")
for i in range(1, 11):
     print(f"{num} x {i} = {num*i}")



# Using while loop
print(f"Multiplication table of {num} using while loop:")
i = 1
while i <= 10:
     print(f"{num} x {i} = {num*i}")
     i += 1



     
# Using list comprehension     
print(f"Multiplication table of {num} using list comprehension:")
print([f"{num} x {i} = {num*i}" for i in range(1, 11)])