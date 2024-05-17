n = int(input())
points = [list(map(float, input().split())) for _ in range(n)]
parent = [i for i in range(n)]
mst = []
edges = []
for i in range(n-1):
  for j in range(i+1, n):
    distance = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
    distance = distance**0.5
    edges.append((distance, i, j))
edges.sort(key=lambda x:x[0])

def find(x):
  if x == parent[x]: return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x != y:
    parent[x] = y
  
for c, a, b in edges:
  if find(a) == find(b): continue
  union(a, b)
  mst.append(c)
  if len(mst) == n-1: break

print(sum(mst))