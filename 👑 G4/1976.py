n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

def find(x):
  if x == parent[x]: return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x != y:
    parent[x] = y

for i in range(n):
  temp = list(map(int, input().split()))
  for j in range(n):
    if temp[j] == 1:
      union(i+1, j+1)
  
path = list(map(int, input().split()))

for i in range(m-1):
  if find(path[i]) != find(path[i+1]):
    print("NO")
    break
else:
  print("YES")