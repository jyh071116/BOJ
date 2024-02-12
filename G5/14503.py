n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1
visited[r][c] = 1
while True:
  for _ in range(4):
    d = (d - 1) % 4
    nx = r + dx[d]
    ny = c + dy[d]
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        r, c = nx, ny
        visited[r][c] = 1
        cnt += 1
        break
  else:
    if arr[r - dx[d]][c - dy[d]] == 1:
      break
    else:
      r, c = r - dx[d], c - dy[d]
print(cnt)