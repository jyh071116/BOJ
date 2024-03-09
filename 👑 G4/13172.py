import sys
input = sys.stdin.readline

m = int(input())
p = 1000000007
res = 0
def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a%b)

def powmod(a, n, p):
  if n == 1: return a % p
  temp = powmod(a, n//2, p) % p
  if n % 2 == 1:
    return temp * temp % p * a % p
  else:
    return temp * temp % p

for _ in range(m):
  a, b = map(int, input().split())
  gcd = gcd(a, b)
  a //= gcd
  b //= gcd
  res += b % p * powmod(a, p-2, p) % p
  res %= p

print(res)