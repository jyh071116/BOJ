n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])

parent = [i for i in range(n+1)]
mst = []

def find(x):
  if x == parent[x]: return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x != y:
    parent[x] = y

for a, b, c in edges:
  if len(mst) == n-2: break
  if find(a) == find(b): continue
  mst.append(c)
  union(a, b)

print(sum(mst))