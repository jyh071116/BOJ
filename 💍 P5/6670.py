import sys
input = sys.stdin.readline

def eea(a, b, s1, s2, t1, t2):
    if b == 0:
      return a, s1, t1
    q = a//b
    s = s1 - s2*q
    t = t1 - t2*q
    return eea(b, a%b, s2, s, t2, t)

while True:
  a, b, c, k = map(int, input().split())
  if a == 0 and b == 0 and c == 0 and k == 0:
    break
  m = 2**k
  d = (b-a)%m

  if a == b:
    print(0)
  elif c == 0:
    print("FOREVER")
  else:
    gcd, s, t = eea(c, m, 1, 0, 0, 1)
    if d % gcd != 0:
      print("FOREVER")
    else:
      print((s*(d//gcd)) % m % (m//gcd))