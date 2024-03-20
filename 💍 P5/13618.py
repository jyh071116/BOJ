n, e, c = map(int, input().split())
_max = int(n**0.5)
isPrime = [1]*(_max+1)

def powmod(a, n, mod):
  res = 1
  while n:
    if n % 2 == 1: res = res * a % mod
    n //= 2
    a = a * a % mod
  return res

def eea(a, b, s1, s2, t1, t2):
  if b == 0:
    return a, s1, t1
  q = a//b
  s = s1 - s2*q
  t = t1 - t2*q
  return eea(b, a%b, s2, s, t2, t)

for i in range(2, int(_max**0.5)+1):
  if isPrime[i]:
    j = 2
    while i*j <= _max:
      isPrime[i*j] = 1
      j += 1

for i in range(3, _max+1, 2):
  if isPrime[i] and n % i == 0:
    p = i
    q = n//p
    break

totient = (p-1)*(q-1)
gcd, d, t = eea(e, totient, 1, 0, 0, 1)
print(powmod(c, d%totient, n))