import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = [i for i in range(n)]
def find(x):
  if x == parent[x]: return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x != y:
    parent[x] = y

for i in range(1, m+1):
  x, y = map(int, input().split())
  if find(x) == find(y):
    print(i)
    break
  union(x, y)
else:
  print(0)