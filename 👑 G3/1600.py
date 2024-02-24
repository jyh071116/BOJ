from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]

q = deque([(0, 0, k)])

while q:
  x, y, horse_move = q.popleft()
  if x == h-1 and y == w-1:
    print(visited[x][y][horse_move])
    break
  
  if horse_move:
    for a, b in [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1), (x+1, y+2), (x-1, y+2), (x+1, y-2), (x-1, y-2)]:
      if 0<=a<h and 0<=b<w and arr[a][b] != 1 and not visited[a][b][horse_move-1]:
        visited[a][b][horse_move-1] = visited[x][y][horse_move] + 1
        q.append((a, b, horse_move-1))
  
  for a, b in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
    if 0<=a<h and 0<=b<w and arr[a][b] != 1 and not visited[a][b][horse_move]:
        visited[a][b][horse_move] = visited[x][y][horse_move] + 1
        q.append((a, b, horse_move))
else:
  print(-1)