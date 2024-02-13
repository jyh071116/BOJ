import sys
sys.setrecursionlimit(10**9)

n = int(input())
tree = {}
for _ in range(n-1):
  parent, child, w = map(int, input().split())
  try:
    tree[parent].append((child, w))
  except:
    tree[parent] = [(child, w)]
  
  try:
    tree[child].append((parent, w))
  except:
    tree[child] = [(parent, w)]

def dfs(n, distance):
  if not tree.get(n):
    return
  
  for node, w in tree[n]:
    if visited[node] == -1:
      visited[node] = distance + w
      dfs(node, distance + w)

visited = [-1]*(n+1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1]*(n+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))