from collections import deque

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited = [[float('inf')]*c for _ in range(r)]

person_q = deque([])
fire_q = deque([])
for i in range(r):
  for j in range(c):
    if arr[i][j] == "J":
      arr[i][j] = "."
      person_q.append((i, j, 0))
    elif arr[i][j] == "F":
      fire_q.append((i, j, 0))

while fire_q:
  x, y, time = fire_q.popleft()
  
  for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
    if 0<=a<r and 0<=b<c and visited[a][b] > time + 1 and arr[a][b] == ".":
        visited[a][b] = time + 1
        fire_q.append((a, b, time+1))

while person_q:
  x, y, time = person_q.popleft()
  if x == -1 or x == r or y == -1 or y == c:
    print(time)
    break
  
  for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
    if a == -1 or a == r or b == -1 or b == c:
      person_q.append((a, b, time+1))
    elif 0<=a<r and 0<=b<c and visited[a][b] > time + 1 and arr[a][b] == ".":
        visited[a][b] = time + 1
        person_q.append((a, b, time+1))
else:
  print("IMPOSSIBLE")