def powmod(a, n, p):
  if n == 1: return a % p
  temp = powmod(a, n//2, p)
  if n % 2 == 1:
    return temp * temp * a % p
  else:
    return temp * temp % p

while True:
  p, a = map(int, input().split())
  isPrime = True
  if p == 0 and a == 0:
    break
  for i in range(2, int(p**0.5)+1):
    if p % i == 0:
      isPrime = False
      break
  
  if isPrime:
    print("no")
  elif powmod(a, p, p) == a:
    print("yes")
  else:
    print("no")