import sys
input = sys.stdin.readline

n, c = map(int, input().split())
pos = [int(input()) for _ in range(n)]
pos.sort()

start = 1
end = pos[-1]-pos[0]

while start <= end:
  mid = (start + end) // 2
  cnt = 1
  current = pos[0]
  
  for i in range(1, n):
    if pos[i] - current >= mid:
      cnt += 1
      current = pos[i]
  
  if cnt >= c:
    start = mid + 1
  else:
    end = mid - 1

print(end)