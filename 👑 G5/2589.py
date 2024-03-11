from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
min_val = float('inf')
res = 0

for i in range(n):
  for j in range(m):
    if arr[i][j] == "L":
      temp_res = 0
      visited = [[0]*m for _ in range(n)]
      visited[i][j] = 1
      q = deque([(i, j, 0)])
      while q:
        x, y, depth = q.popleft()
        temp_res = max(temp_res, depth)
        for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
          if 0<=a<n and 0<=b<m and arr[a][b] == "L" and not visited[a][b]:
            visited[a][b] = 1
            q.append((a, b, depth+1))
      res = max(res, temp_res)

print(res)