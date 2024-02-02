import sys
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
parent = [0]*(n+1)

for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(n):
  visited[n] = 1
  for i in graph[n]:
    if not visited[i]:
      parent[i] = n
      dfs(i)

dfs(1)
for i in range(2, n+1):
  print(parent[i])