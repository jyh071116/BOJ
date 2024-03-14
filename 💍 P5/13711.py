from bisect import bisect_left

n = int(input())
standard = [0]*(n+1)
res = [0]*n
a = list(map(int, input().split()))
for i in range(n):
  standard[a[i]] = i
b = list(map(int, input().split()))
for i in range(n):
  res[i] = standard[b[i]]

dp = [1]
x = [a[0]]

for i in range(1, n):
  if res[i] > x[-1]:
    x.append(res[i])
    dp.append(dp[-1]+1)
  else:
    idx = bisect_left(x, res[i])
    x[idx] = res[i]

print(dp[-1])