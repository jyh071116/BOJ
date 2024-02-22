from collections import deque

while True:
  l, r, c = map(int, input().split())
  if l == 0 and r == 0 and c == 0:
    break
  arr = []
  visited = [[[0]*c for _ in range(r)] for _ in range(l)]
  for _ in range(l):
    arr.append([list(input()) for _ in range(r)])
    input()
  
  q = deque([])
  escape = []
  
  for i in range(l):
    for j in range(r):
      for k in range(c):
        if arr[i][j][k] == "S":
          q.append((i, j, k, 0))
        if arr[i][j][k] == "E":
          escape = [i, j, k]
  
  while q:
    x, y, z, time = q.popleft()
    if x == escape[0] and y == escape[1] and z == escape[2]:
      print(f'Escaped in {time} minute(s).')
      break
    
    for nx, ny, nz in [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]:
      if 0<=nx<l and 0<=ny<r and 0<=nz<c and arr[nx][ny][nz] != "#" and not visited[nx][ny][nz]:
        visited[nx][ny][nz] = 1
        q.append((nx, ny, nz, time+1))
  else:
    print("Trapped!")