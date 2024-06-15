import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

while True:
  m, n = map(int, input().split())
  if m == 0 and n == 0: break
  edges = []
  mst = []
  for _ in range(n):
    x, y, z = map(int, input().split())
    edges.append([z, x, y])
  edges.sort(key=lambda x:x[0])

  parent = [i for i in range(m)]

  def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

  def union(x, y):
    x = find(x)
    y = find(y)
    if x != y: parent[x] = y

  for z, x, y in edges:
    if find(x) == find(y): continue
    mst.append(z)
    union(x, y)
    if len(mst) == m-1: break

  print(sum([i[0] for i in edges]) - sum(mst))