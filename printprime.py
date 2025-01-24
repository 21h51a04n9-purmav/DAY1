import math
def prime(n):
   if n<=1:
      return False
   for i in range(2,int(n**0.5)+1):
      if n%i==0:
         return False
   return True
def print_primes(m,n):
   for n in range(m,n+1):
      if prime(n):
         print(n)
m=int(input())
n=int(input())
print_primes(m,n)