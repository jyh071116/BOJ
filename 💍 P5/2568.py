from bisect import bisect_left

n = int(input())
a = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
d = [0]*(n+1)
dp = [0]
x = [0]
a.sort(key=lambda x:x[0])

for i in range(1, n+1):
  if a[i][1] > x[-1]:
    x.append(a[i][1])
    d[i] = dp[-1]+1
    dp.append(dp[-1]+1)
  else:
    idx = bisect_left(x, a[i][1])
    d[i] = dp[idx]
    x[idx] = a[i][1]

print(n-dp[-1])
lst = []
for i in range(n, 0, -1):
    if d[i] == dp[-1]:
      lst.append(a[i][0])
      dp.pop()

for i in list(set([i for i, _ in a[1:]]) - set(sorted(lst))):
  print(i)