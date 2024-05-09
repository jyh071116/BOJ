from collections import deque

n = int(input())
arr = list(map(int, input().split()))
visited = [0]*n

q = deque([(0, 0)])
while q:
  depth, idx = q.popleft()
  if idx == n-1:
    print(depth)
    break
  for x in range(1, arr[idx]+1):
    if 0 < idx+x < n and not visited[idx+x]:
      visited[idx+x] = 1
      q.append((depth+1, idx+x))
else:
  print(-1)