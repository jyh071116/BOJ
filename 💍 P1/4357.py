import math

def powmod(a, n, mod):
  res = 1
  while n:
    if n % 2 == 1: res = res * a % mod
    n //= 2
    a = a * a % mod
  return res

def discrete_log(p, b, n):
  k = math.ceil(p**0.5)
  s = set([])
  
  t = 1
  for i in range(k):
    s.add(t)
    t = t * b % p

  t = 1
  for i in range(k):
    x = n * t % p
    if x in s:
      temp = 1
      for j in range(k):
        if temp == x:
          return i*k+j
        temp = temp * b % p
    else:
      t = t * pow(pow(b, k, p), p-2, p) % p
  return "no solution"

while True:
  try:
    p, b, n = map(int, input().split())
    print(discrete_log(p, b, n))
  except:
    break