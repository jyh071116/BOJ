import bisect

n, t = map(int, input().split())
arr = []
for _ in range(n):
  s, i, c = map(int, input().split())
  for j in range(c):
    arr.append(s + i*j)
arr.sort()

idx = bisect.bisect_left(arr, t)
try:
  print(arr[idx]-t)
except:
  print(-1)