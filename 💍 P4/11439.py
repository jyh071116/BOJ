n, k, m = map(int, input().split())
primes = [1]*(n+1)
cnt = {}
res = 1

def power(a, n, mod):
  res = 1
  while n:
    if n % 2 == 1: res = res * a % mod
    n //= 2
    a = a * a % mod
  return res

for i in range(2, int(n**0.5)+1):
  if primes[i]:
    j = 2
    while i*j <= n:
      primes[i*j] = 0
      j += 1

for i in range(2, n+1):
  if primes[i]:
    cnt[i] = 0
    j = i
    while j <= n:
      cnt[i] += n//j - k//j - (n-k)//j
      j *= i

for i in cnt.keys():
  res *= pow(i, cnt[i], m)
  res %= m
print(res)