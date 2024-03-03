t = int(input())
max = 330000
isPrime = [1]*(max+1)
isPrime[0], isPrime[1] = 0, 0
prime = []
superPrime = []

for i in range(2, int(max**0.5)+1):
  if isPrime[i]:
    j = 2
    while i*j <= max:
      isPrime[i*j] = 0
      j += 1

for i in range(max+1):
  if isPrime[i]:
      prime.append(i)
      
for i in range(len(prime)):
  if isPrime[i+1]:
    superPrime.append(prime[i])

for _ in range(t):
  print(superPrime[int(input())-1])