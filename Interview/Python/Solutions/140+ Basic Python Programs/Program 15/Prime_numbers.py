# print prime numbers in a given range
def is_prime(n):
     if n <= 1:
          return False
     for i in range(2, n):
            if n % i == 0:
                return False
     return True
print("Prime numbers in the range are: ")
n = int(input("Enter the range: "))
for i in range(1, n):
     if is_prime(i):
          print(i)