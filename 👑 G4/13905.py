import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
s, e = map(int, input().split())

edges = []
mst = []
for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append([c, a, b])
edges.sort(reverse=True, key=lambda x:x[0])

parent = [i for i in range(n+1)]

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
  if find(s) == find(e):
    print(min(mst))
    break
else:
  print(0)