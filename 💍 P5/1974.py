from bisect import bisect_left

t = int(input())
for _ in range(t):
  n = int(input())
  a = [0] + list(map(int, input().split()))
  d = [0]*(n+1)
  dp = [0]
  x = [0]

  for i in range(1, n+1):
    if a[i] > x[-1]:
      x.append(a[i])
      d[i] = dp[-1]+1
      dp.append(dp[-1]+1)
    else:
      idx = bisect_left(x, a[i])
      d[i] = dp[idx]
      x[idx] = a[i]

  print(dp[-1])
  lst = []
  for i in range(n, 0, -1):
    if d[i] == dp[-1]:
      lst.append(i)
      dp.pop()
  print(*sorted(lst))