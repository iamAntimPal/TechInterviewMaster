# Python program to check if a year is a leap year

# Input from user
year = int(input("Enter a year: "))

# Check leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is Not a Leap Year.")

# Output
# Enter a year: 2020
# 2020 is a Leap Year.

# Enter a year: 2019
# 2019 is Not a Leap Year.
