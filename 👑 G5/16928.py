from collections import deque

n, m = map(int, input().split())
arr = [0]*(101)
for _ in range(n):
  x, y = map(int, input().split())
  arr[x] = y
for _ in range(m):
  u, v = map(int, input().split())
  arr[u] = v

visited = [0]*(101)
q = deque([(1, 0)])
while q:
  x, depth = q.popleft()
  for i in [(x+1), (x+2), (x+3), (x+4), (x+5), (x+6)]:
    if i == 100:
      print(depth+1)
      exit()
    if i < 100:
      while arr[i] != 0:
        i = arr[i]
      if not visited[i]:
        visited[i] = 1
        q.append((i, depth+1))