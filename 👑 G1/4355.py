max_val = int(10**4.5)
primes = [1]*(max_val+1)
for i in range(2, int(max_val**0.5)+1):
  if primes[i]:
    j = 2
    while i*j <= max_val:
      primes[i*j] = 0
      j += 1

while True:
  n = int(input())
  if n == 0:
    break
  if n == 1:
    print(0)
    continue
  factor = {}
  while n != 1:
    for i in range(2, max_val+1):
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