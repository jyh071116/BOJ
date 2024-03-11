from collections import deque

t = int(input())
for _ in range(t):
  n = int(input())
  visited = [[0]*n for _ in range(n)]
  x, y = map(int, input().split())
  destination = list(map(int, input().split()))
  
  q = deque([(x, y, 0)])
  while q:
    x, y, depth = q.popleft()
    if x == destination[0] and y == destination[1]:
      print(depth)
      break
    
    for a, b in [(x+2, y-1), (x+2, y+1), (x-2, y+1), (x-2, y-1), (x+1, y+2), (x-1, y+2), (x+1, y-2), (x-1, y-2)]:
      if 0<=a<n and 0<=b<n and not visited[a][b]:
        visited[a][b] = 1
        q.append((a, b, depth+1))