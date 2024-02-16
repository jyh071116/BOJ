import sys
input = sys.stdin.readline

n, k = map(int, input().split())
scores = list(map(int, input().split()))
start, mid, end = 0, 0, 10**12

while start < end:
  mid = (start + end) // 2
  cnt = 0
  for score in scores:
    if score > mid:
      cnt += score - mid
      
  if cnt <= k:
    end = mid
  else:
    start = mid + 1

print(start)