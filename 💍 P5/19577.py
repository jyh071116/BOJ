n = int(input())
max_val = int(n**0.5)
primes = [1]*(max_val+1)
n_factor = []

for i in range(1, max_val+1):
  if n % i == 0:
    n_factor.append(i)
    if (i != n//i): n_factor.append(n//i)

n_factor.sort()

for i in range(2, max_val+1):
  if primes[i]:
    j = 2
    while i*j <= max_val:
      primes[i*j] = 0
      j += 1
      
for i in n_factor:
  if n % i == 0:
    factor = {}
    res = 1
    n_divided_i = n//i
    while i != 1:
      for j in range(2, max_val+1):
        if primes[j] and i % j == 0:
          try:
            factor[j] += 1
          except:
            factor[j] = 1
          i //= j
          break
      else:
        factor[i] = 1
        break
    
    for j in factor.keys():
      res *= j**factor[j] - j**(factor[j]-1)
      
    if res == n_divided_i:
      print(n//n_divided_i)
      exit(0)

print(-1)