import math
t = int(input())

fibo = [0]*45
fibo[1], fibo[2] = 1, 1
for i in range(3, 45):
  fibo[i] = fibo[i-1] + fibo[i-2]
  
def eea(a, b, s1, s2, t1, t2):
  if b == 0:
    return a, s1, t1
  q = a//b
  s = s1 - s2*q
  t = t1 - t2*q
  return eea(b, a%b, s2, s, t2, t)

for _ in range(t):
  n = int(input())
  res = [float('inf'), float('inf')]
  for i in range(3, 45):
    gcd, s, t = eea(fibo[i-2], fibo[i-1], 1, 0, 0, 1)
    s *= n
    t *= n
    k = min(math.ceil(-s/fibo[i-1]), math.ceil(t/fibo[i-2]))
    s += fibo[i-1]*k
    t -= fibo[i-2]*k

    if 0 <= s and 0 <= t and s+t < res[0]+res[1]:
      res = [s, t]
  
  if res[0] > res[1] or res[0] == 0:
    print(res[1], res[0]+res[1])
  else:
    print(*res)