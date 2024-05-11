v, e = map(int, input().split())
edges = []
mst = []
for _ in range(e):
  a, b, c = map(int, input().split())
  edges.append([c, a, b])
edges.sort(key=lambda x:x[0])

parent = [i for i in range(v+1)]

def find(x):
  if x == parent[x]: return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x != y: parent[x] = y

for c, a, b in edges:
  if find(a) == find(b): continue
  mst.append(c)
  union(a, b)
  if len(mst) == v-1: break

print(sum(mst))