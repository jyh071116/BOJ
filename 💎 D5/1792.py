t = int(input())
max = 50000

mu = [0]*(max+1)
mu[1] = 1
for i in range(1, max+1):
  for j in range(i*2, max+1, i):
    mu[j] -= mu[i]
  mu[i] += mu[i-1]

for _ in range(t):
  a, b, d = map(int, input().split())
  n = min(a//d, b//d)
  sum = 0
  i = 1
  while i <= n:
    j = min(a//(a//i), b//(b//i))
    sum += (mu[j] - mu[i-1]) * (a//(d*i)) * (b//(d*i))
    i = j + 1
  print(sum)