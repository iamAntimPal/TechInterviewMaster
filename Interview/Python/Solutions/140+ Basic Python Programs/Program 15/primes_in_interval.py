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

# Prime number function from 1 to 10 prime numbers

def prime_in_interval(start, end):
     # Create a boolean array to store the prime numbers
     prime = [True for i in range(end + 1)]
      p = 2
      while (p * p <= end):
          # If prime[p] is not changed, then it is a prime
          if (prime[p] == True):
              # Update all multiples of p
              for i in range(p * 2, end + 1, p):
                  prime[i] = False
          p += 1
      # Print all prime numbers in the given interval
      prime_numbers = []
      for p in range(start, end + 1):
          if prime[p]:
              prime_numbers.append(p)
      return prime_numbers

# Driver code
if __name__ == '__main__':
    start = 10
    end = 50
    prime_numbers = prime_in_interval(start, end)
    print(prime_numbers)
