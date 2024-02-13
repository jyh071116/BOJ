n = int(input())
tree = {}
visited = [-1]*(n+1)
for _ in range(n):
  temp = list(map(int, input().split()))
  tree[temp[0]] = [(temp[1], temp[2])]
  i = 3
  while temp[i] != -1:
    tree[temp[0]].append((temp[i], temp[i+1]))
    i += 2

def dfs(n, dis):
  for num, distance in tree[n]:
    if visited[num] == -1:
      visited[num] = dis+distance
      dfs(num, dis+distance)

visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1]*(n+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))