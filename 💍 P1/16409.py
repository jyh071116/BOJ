a, b, c, d = map(int, input().split())
n = min(b, d)
res = 0

mu = [0]*(n+1)
mu[1] = 1
for i in range(1, n+1):
  for j in range(i*2, n+1, i):
    mu[j] -= mu[i]

for i in range(1, min(b, d)+1):
  res += mu[i] * ((b//i) - ((a-1)//i)) * ((d//i) - ((c-1)//i))

print(res)