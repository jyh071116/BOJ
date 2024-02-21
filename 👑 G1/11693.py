n, m = map(int, input().split())
p = 1000000007
res = 1

def pow(a, n, mod):
  res = 1
  while n:
    if n % 2 == 1:
      res = res * a % mod
    n //= 2
    a = a * a % mod
  return res

for i in range(2, int(n**0.5)+1):
  if n == 1:
    break
  e = 0
  while n % i == 0:
    n //= i
    e += 1
  if e != 0:
    res = (res * (pow(i, e*m+1, p)-1) * (pow(i-1, p-2, p))) % p

if n != 1:
  res = (res * (pow(n, m+1, p)-1) * (pow(n-1, p-2, p))) % p
print(res)