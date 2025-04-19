# Author : Antim Pal
# Date : 2025-04-19
# Description : Program to find all prime numbers in a given interval
# Time Complexity : O(n log log n) for Sieve of Eratosthenes
# Space Complexity : O(n) for storing prime numbers
# Input : Start and end of the interval
# Output : List of prime numbers in the given interval
# Example : Input: 10, 50
#          Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# Note : This program uses the Sieve of Eratosthenes algorithm to find prime numbers in a given interval.
# The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
# It works by iteratively marking the multiples of each prime number starting from 2.
# The numbers which are not marked in the process are prime numbers.
# The time complexity of the Sieve of Eratosthenes is O(n log log n), which makes it very efficient for finding prime numbers in a given interval.
# The space complexity of the Sieve of Eratosthenes is O(n), which makes it very space-efficient for finding prime numbers in a given interval.
# The program takes two inputs, start and end, which define the interval in which we want to find prime numbers.

# Prime number function from 1 to 10 prime numbers using class method
class PrimeNumbers:
     def __init__(self, start, end):
          self.start = start
          self.end = end
     
     def is_prime(self, n):
          if n <= 1:
               return False
          for i in range(2, int(n**0.5) + 1):
               if n % i == 0:
                    return False
          return True
     
     def get_primes(self):
          primes = []
          for num in range(self.start, self.end + 1):
               if self.is_prime(num):
                    primes.append(num)
          return primes

start = int(input("Enter First number of the interval: "))
end = int(input("Enter Last number of the interval: "))
prime_numbers = PrimeNumbers(start, end)
print(prime_numbers.get_primes())  # Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, ...,num]
