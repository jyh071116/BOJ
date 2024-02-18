n = int(input())
primes = [1]*(n+1)
cnt = 0

for i in range(2, n+1):
  if primes[i]:
    j = 2
    while i*j <= n:
      primes[i*j] = 0
      j += 1

for i in range(2, n+1):
  factor = {}
  phi = 1
  while i != 1:
    for j in range(2, n+1):
      if primes[j] and i % j == 0:
        try:
          factor[j] += 1
        except:
          factor[j] = 1
        i //= j
        break
  
  for j in factor.keys():
    phi *= j**factor[j] - j**(factor[j]-1)
  cnt += phi

print(cnt)