def eea(a, b):
  if a == 0:
    return b, 0, 1
  else:
    gcd, x, y = eea(b % a, a)
    return gcd, y - (b // a) * x, x
  
t = int(input())
for _ in range(t):
  k, c = map(int, input().split())
  gcd, x, y = eea(k, c)
  if c == 1:
    if k >= 10**9:
      print("IMPOSSIBLE")
    else:
      print(k+1)
  elif k == 1:
    print(1)
  elif gcd != 1:
    print("IMPOSSIBLE")
  else:
    while y < 0:
      y = y+k
    if y == 0 or y == 10**9:
      print("IMPOSSIBLE")
    print(y)