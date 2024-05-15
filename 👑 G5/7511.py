import sys
input = sys.stdin.readline
t = int(input())

def find(x):
  if x == parent[x]: return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x != y:
    parent[x] = y

for i in range(t):
  n = int(input())
  k = int(input())
  parent = [i for i in range(n)]
  for _ in range(k):
    a, b = map(int, input().split())
    union(a, b)
  m = int(input())
  print(f'Scenario {i+1}:')
  for _ in range(m):
    u, v = map(int, input().split())
    if find(u) == find(v):
      print(1)
    else:
      print(0)
  print()