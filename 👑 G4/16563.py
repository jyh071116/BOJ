n = int(input())
arr = list(map(int, input().split()))
max_val = max(arr)

primes = [float('inf')]*(max_val+1)

for i in range(2, int(max_val**0.5)+1):
  if primes[i] == float('inf'):
    j = 1
    while i*j <= max_val:
      primes[i*j] = min(primes[i*j], i)
      j += 1

for item in arr:
  while item > 1:
    if primes[item] == float('inf'):
      print(item, end=" ")
      item = 1
    else:
      print(primes[item], end=" ")
      item //= primes[item]
  print()