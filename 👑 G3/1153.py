n = int(input())
isPrime = [1]*(n+1)
primes = []
ans = []
impossible = 0

for i in range(2, int(n**0.5)+1):
  if isPrime[i]:
    j = 2
    while i*j <= n:
      isPrime[i*j] = 0
      j += 1

for i in range(n, 1, -1):
  if isPrime[i]:
    primes.append(i)

while n != 0:
  for prime in primes:
    if n-prime >= 2*(3-len(ans)):
      n -= prime
      ans.append(prime)
      break
  else:
    ans = [-1]
    break

print(*sorted(ans))