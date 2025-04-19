# Leap year Question using Python function
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.

# A year is a leap year if it is divisible by 4 and not divisible by 100, or it is divisible by 400.

def is_LeapYear(year):
     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
          return True
     else:
          return False
year = int(input("Enter a year: "))
print("The year", year, "is a leap year." if is_LeapYear(year) else "is not a leap year.")


