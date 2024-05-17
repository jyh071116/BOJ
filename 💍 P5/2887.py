n = int(input())
X = []
Y = []
Z = []
for i in range(n):
  x, y, z = map(int, input().split())
  X.append((x, i))
  Y.append((y, i))
  Z.append((z, i))
X.sort(key=lambda x:x[0])
Y.sort(key=lambda x:x[0])
Z.sort(key=lambda x:x[0])

parent = [i for i in range(n)]
mst = []
edges = []
for i in range(n-1):
  distance_x = X[i+1][0]-X[i][0]
  edges.append((distance_x, X[i][1], X[i+1][1]))
  distance_y = Y[i+1][0]-Y[i][0]
  edges.append((distance_y, Y[i][1], Y[i+1][1]))
  distance_z = Z[i+1][0]-Z[i][0]
  edges.append((distance_z, Z[i][1], Z[i+1][1]))
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