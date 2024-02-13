import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max = 0
max_cnt = 0
for i in arr:
  for j in i:
    if j > max: max = j

def dfs(depth, x, y):
  if 0<=x<n and 0<=y<n and not visited[x][y] and arr[x][y] > depth:
    visited[x][y] = 1
    for i, j in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
      dfs(depth, i, j)
    return 1
  return 0

for depth in range(0, max):
  visited = [[0 for _ in range(n)] for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(n):
      cnt += dfs(depth, i, j)
  
  if cnt > max_cnt: max_cnt = cnt

print(max_cnt)