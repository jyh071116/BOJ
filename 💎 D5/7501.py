a, b = map(int, input().split())
lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def power(a, n, mod):
  res = 1
  while n:
    if n % 2 == 1:
      res = res * a % mod
    n //= 2
    a = a * a % mod
  return res

def millor(n, a):
  if a % n == 0: return True
  k = n-1
  temp = power(a, k, n)
  while True:
    if temp == n-1:
      return True
    if k % 2 == 1:
      return (temp == 1 or temp == n-1)
    k //= 2

if a % 2 == 0: a += 1
for i in range(a, b+1, 2):
  isPrime = True
  for a in lst:
    if not isPrime:
      break
    isPrime &= millor(i, a)
    
  if isPrime or i == 9:
    print(i, end=" ")