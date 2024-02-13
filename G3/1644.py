n = int(input())
primes = [1]*(n+1)
primes[0], primes[1] = 0, 0
prime = []
cnt = 0
for i in range(2, int(n**0.5)+1):
  if primes[i]:
    j = 2
    while i*j <= n:
      primes[i*j] = 0
      j += 1

for i in range(n+1):
  if primes[i]:
    prime.append(i)

for i in range(len(prime)):
  sum = 0
  while sum < n and i < len(prime):
    sum += prime[i]
    i += 1
  if sum == n:
    cnt += 1

print(cnt)