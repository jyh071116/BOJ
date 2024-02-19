import random

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
      return (temp == 1 or temp == n-1)
    k //= 2

def isPrime(n):
  if n == 1: return False
  for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
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
    
    if n == d:
      return pollard(n)
  if isPrime(d):
    return d
  else:
    return pollard(d)

while True:
  p = int(input())
  if p == 0:
    break
  n = p
  factor = {}
  divisors = []
  while n != 1:
    temp = pollard(n)
    try:
      factor[temp] += 1
    except:
      factor[temp] = 1
    n //= temp
  
  keys = list(factor.keys())
  
  def dfs(pos, divisor):
    if pos == len(keys):
      divisors.append(divisor)
      return
    for i in range(factor[keys[pos]]+1):
      dfs(pos+1, divisor*(keys[pos]**i))
  
  dfs(0, 1)
  divisors.sort()
  
  res = float('inf')
  for d in divisors:
    k = p//d
    start, end = 0, len(divisors)-1
    while start < end:
      mid = (start + end) // 2
      
      if divisors[mid] < k**0.5:
        start = mid+1
      else:
        end = mid
    
    gap = 0
    while end-gap >= 0 or end+gap < len(divisors):
      isBreak = False
      if end-gap >= 0 and k % divisors[end-gap] == 0:
        w = divisors[end-gap]
        h = k//w
        res = min(res, w+d+h)
        isBreak = True
      if end+gap < len(divisors) and k % divisors[end+gap] == 0:
        w = divisors[end+gap]
        h = k//w
        res = min(res, w+d+h)
        isBreak = True
      
      if isBreak: break
      gap += 1

  print(res)