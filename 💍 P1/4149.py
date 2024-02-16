import random
import sys
input = sys.stdin.readline

n = int(input())
lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
res = []

def power(a, n, mod):
  res = 1
  while n:
    if n % 2 == 1:
      res = res * a % mod
    n //= 2
    a = a * a % mod
  return res

def millor(n, a):
  if a % n == 0:
    return True
  k = n-1
  while True:
    temp = power(a, k, n)
    if temp == n-1: return True
    if k % 2 == 1: return (temp == 1 or temp == n-1)
    k //= 2

def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a%b)

def isPrime(n):
  if n == 1: return False
  for a in lst:
    if not millor(n, a):
      return False
  return True

def pollard(n):
  if n % 2 == 0:
    return 2
  if isPrime(n):
    return n
  
  c = random.randrange(1, n)
  x = random.randrange(2, n)
  y = x
  d = 1
  
  while d == 1:
    x = (x*x+c)%n
    y = (y*y+c)%n
    y = (y*y+c)%n
    d = gcd(abs(x-y), n)
    
    if d==n:
      return pollard(n)
  if isPrime(d):
    return d
  else:
    return pollard(d)

while n != 1:
  factor = pollard(n)
  res.append(factor)
  n //= factor

res.sort()
for i in res:
  print(i)