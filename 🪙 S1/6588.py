import sys
input = sys.stdin.readline

max = 1000000
isPrime = [1]*(max+1)

for i in range(2, int(max**0.5)+1):
  if isPrime[i]:
    j = 2
    while i*j <= max:
      isPrime[i*j] = 0
      j += 1

while True:
  n = int(input())
  if n == 0:
    break
  for i in range(3, n//2+1):
    if isPrime[i] and isPrime[n-i]:
      print(f'{n} = {i} + {n-i}')
      break
  else:
    print("Goldbach's conjecture is wrong.")