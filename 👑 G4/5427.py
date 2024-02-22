from collections import deque

t = int(input())
for _ in range(t):
  w, h = map(int, input().split())
  arr = [list(input()) for _ in range(h)]
  visited = [[float('inf')]*w for _ in range(h)]
  
  person_q = deque([])
  fire_q = deque([])
  for i in range(h):
    for j in range(w):
      if arr[i][j] == "@":
        arr[i][j] = "."
        person_q.append((i, j, 0))
      elif arr[i][j] == "*":
        fire_q.append((i, j, 0))

  while fire_q:
    x, y, time = fire_q.popleft()
    
    for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
      if 0<=a<h and 0<=b<w and visited[a][b] > time + 1 and arr[a][b] == ".":
          visited[a][b] = time + 1
          fire_q.append((a, b, time+1))
  
  while person_q:
    x, y, time = person_q.popleft()
    if x == -1 or x == h or y == -1 or y == w:
      print(time)
      break
    
    for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
      if a == -1 or a == h or b == -1 or b == w:
        person_q.append((a, b, time+1))
      elif 0<=a<h and 0<=b<w and visited[a][b] > time + 1 and arr[a][b] == ".":
          visited[a][b] = time + 1
          person_q.append((a, b, time+1))
  else:
    print("IMPOSSIBLE")