t = int(input())
max = 10000
isPrime = [1]*(max+1)

for i in range(2, int(max**0.5)+1):
  if isPrime[i]:
    j = 2
    while i*j <= max:
      isPrime[i*j] = 0
      j += 1

for _ in range(t):
  n = int(input())
  for i in range(n//2, 1, -1):
    if isPrime[i] and isPrime[n-i]:
      print(i, n-i)
      break