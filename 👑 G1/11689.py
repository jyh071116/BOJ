n = int(input())
primes = [1]*(10**6+1)
factor = {}
for i in range(2, 10**3+1):
  if primes[i]:
    j = 2
    while i*j <= 10**6:
      primes[i*j] = 0
      j += 1


while n != 1:
  for i in range(2, 10**6+1):
    if primes[i] and n % i == 0:
      try:
        factor[i] += 1
      except:
        factor[i] = 1
      n //= i
      break
  else:
    factor[n] = 1
    break

res = 1
for i in factor.keys():
  res *= i**(factor[i]) - i**(factor[i]-1)

print(res)