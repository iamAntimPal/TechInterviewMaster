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
print(prime_numbers.get_primes()) 