import random
import math

n = int(input())
lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def power(a, n, mod):
  res = 1
  while n:
    if n % 2 == 1: res = res * a % mod
    n //= 2
    a = a * a % mod
  return res

def miller(n, a):
  if a % n == 0:
    return True
  k = n-1
  while True:
    temp = power(a, k, n)
    if temp == n-1:
      return True
    if k % 2 == 1:
      return (temp == n-1 or temp == 1)
    k //= 2

def isPrime(n):
  if n == 1:
    return False
  for a in lst:
    if not miller(n, a):
      return False
  return True

def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a%b)

def pollard(n):
  if n % 2 == 0:
    return 2
  if isPrime(n):
    return n
  
  x = random.randrange(2, n)
  y = x
  c = random.randrange(1, n)
  d = 1
  while d == 1:
    x = (x*x+c)%n
    y = (y*y+c)%n
    y = (y*y+c)%n
    d = gcd(abs(x-y), n)
    if d == n:
      return pollard(n)
  
  if isPrime(d):
    return d
  else:
    return pollard(d)

def four(n):
  while n % 4 == 0:
    n //= 4
  return n % 8 == 7

def three(n):
  factor = {}
  while n != 1:
    temp = pollard(n)
    try:
      factor[temp] += 1
    except:
      factor[temp] = 1
    n //= temp
  
  for i in factor.keys():
    if i % 4 == 3 and factor[i] % 2 == 1:
      return True
  return False

if four(n):
  print(4)
elif three(n):
  print(3)
elif int(math.sqrt(n))**2 != n:
  print(2)
else:
  print(1)