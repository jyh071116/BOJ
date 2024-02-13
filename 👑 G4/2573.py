import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
icebergs = set([])
time = 0

for i in range(n):
  for j in range(m):
    if arr[i][j] != 0:
      icebergs.add((i, j))

while True:
  if not icebergs:
    print(0)
    break
  
  melting = []
  for x, y in icebergs:
    speed = 0
    if 0<=x-1<n and 0<=y<m and arr[x-1][y] == 0: speed += 1
    if 0<=x+1<n and 0<=y<m and arr[x+1][y] == 0: speed += 1
    if 0<=x<n and 0<=y-1<m and arr[x][y-1] == 0: speed += 1
    if 0<=x<n and 0<=y+1<m and arr[x][y+1] == 0: speed += 1
    
    melting.append((x, y, speed))
  
  for x, y, speed in melting:
    arr[x][y] -= speed
    if arr[x][y] <= 0:
      arr[x][y] = 0
      icebergs.discard((x, y))
        
  time += 1
  if icebergs:
    visited = [[0]*m for _ in range(n)]
    q = deque([next(iter(icebergs))])
    cnt = 0
    
    while q:
      x, y = q.popleft()
      for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0<=i<n and 0<=j<m and not visited[i][j] and arr[i][j] != 0:
          visited[i][j] = 1
          cnt += 1
          q.append((i, j))
    
    if cnt != len(icebergs):
      print(time)
      break