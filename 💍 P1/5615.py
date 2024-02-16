import sys
input = sys.stdin.readline

q = int(input())
lst = [2, 7, 61]
cnt = 0

def power(a, n, mod):
  res = 1
  a %= mod
  while n:
    if n % 2 == 1:
      res = res * a % mod
    n //= 2
    a = a * a % mod
  return res

def millor(n, a):
  if a % n == 0: return True
  k = n-1
  while True:
    temp = power(a, k, n)
    if temp == n-1: return True
    if k % 2 == 1: return (temp == 1 or temp == n-1)
    k //= 2

for _ in range(q):
    n = int(input())
    isPrime = True
    for a in lst:
      if not isPrime:
        break
      isPrime &= millor(2*n+1, a)
    
    if isPrime: cnt += 1

print(cnt)