a, b = map(int, input().split())
p = 1000000007

def powmod(a, n, p):
  if n == 1: return a % p
  temp = powmod(a, n//2, p) % p
  if n % 2 == 1:
    return temp * temp * a % p
  else:
    return temp * temp % p

if a == 1:
  print(b % p)
else:
  print((((powmod(a, b, p)-1) % p) * powmod(a-1, p-2, p)) % p)