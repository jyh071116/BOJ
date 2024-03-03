n = int(input())
n = max(n, 3)
isPrime = [1]*(n+1)
prime = []
for i in range(2, int(n**0.5)+1):
  if isPrime[i]:
    j = 2
    while i*j <= n:
      isPrime[i*j] = 0
      j += 1

for i in range(2, n+1):
  if isPrime[i]:
    prime.append(i)

for i in range(len(prime)-1):
  res = prime[i]*prime[i+1]
  if res > n:
    print(res)
    break