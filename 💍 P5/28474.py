t = int(input())

def totient(n):
  factor = {}
  while n != 1:
    for i in range(2, int(n**0.5)+1):
      if n % i == 0:
        n //= i
        try:
          factor[i] += 1
        except:
          factor[i] = 1
        break
    else:
      try:
          factor[n] += 1
      except:
        factor[n] = 1
      n = 1
  res = 1
  for i in factor.keys():
    n *= i**factor[i]
    res *= i**factor[i] - i**(factor[i]-1)
  if not factor:
    res = 0
  return res

for _ in range(t):
  n = int(input())
  if n & 1:
    res = totient(n)
  else:
    res = totient(n) + totient(n//2)
  print(res)