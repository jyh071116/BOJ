n, a = map(int, input().split())

def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a%b)

def eea(r1, r2, u1, u2, v1, v2):
  if r2 == 0:
    return u1
  q = r1//r2
  r = r1%r2
  u = u1 - q*u2
  v = v1 - q*v2
  return eea(r2, r, u2, u, v2, v)

덧셈역 = n - (a % n)
if gcd(a, n) == 1:
  곱셈역 = (eea(a, n, 1, 0, 0, 1) + n) % n
else:
  곱셈역 = -1

print(덧셈역, 곱셈역)