a, b, S = map(int, input().split())

def eea(a, b, s1, s2, t1, t2):
  if b == 0:
    return a, s1, t1
  q = a//b
  s = s1-s2*q
  t = t1-t2*q
  return eea(b, a%b, s2, s, t2, t)

def solve():
  if a == 0 and b == 0:
    return S == 0
  if a == 0:
    return S % b == 0
  if b == 0:
    return S % a == 0
  gcd, s, t = eea(a, b, 1, 0, 0, 1)
  if S % gcd != 0:
    return False
  s *= S//gcd
  t *= S//gcd
  for i in range(-gcd*s//b+1, gcd*t//a+1):
    if eea(s+(i*b//gcd), t-(i*a//gcd), 1, 0, 0, 1)[0] == 1:
      return True
  return False

if solve():
  print("YES")
else:
  print("NO")