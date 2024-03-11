from collections import deque

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
water = [[float('inf')]*c for _ in range(r)]
visited = [[0]*c for _ in range(r)]
water_q = deque([])
q = deque([])
for i in range(r):
  for j in range(c):
    if arr[i][j] == "*":
      water[i][j] = 1
      water_q.append((i, j))
    elif arr[i][j] == "D":
      destination = (i, j)
    elif arr[i][j] == "S":
      q.append((i, j, 1))

while water_q:
  x, y = water_q.popleft()
  for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
    if 0<=a<r and 0<=b<c and arr[a][b] == "." and water[a][b] == float('inf'):
      water[a][b] = water[x][y] + 1
      water_q.append((a, b))
while q:
  x, y, depth = q.popleft()
  if arr[x][y] == "D":
    print(depth-1)
    break
  
  for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
    if 0<=a<r and 0<=b<c and arr[a][b] != "X" and depth + 1 < water[a][b] and not visited[a][b]:
      visited[a][b] = 1
      q.append((a, b, depth+1))
else:
  print("KAKTUS")