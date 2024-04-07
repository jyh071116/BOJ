import bisect
t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  b.sort()
  cnt = 0
  for i in a:
    idx = bisect.bisect_left(b, i)
    cnt += idx
  print(cnt)