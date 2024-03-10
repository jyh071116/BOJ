t = int(input())

def find(x):
  if parent[x] == x:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(a, b):
  a = find(a)
  b = find(b)
  
  if a != b:
    parent[b] = a
    cnt[a] += cnt[b]
    cnt[b] = 1
  
  return cnt[a]

for _ in range(t):
  n = int(input())
  parent = {}
  cnt = {}
  for _ in range(n):
    a, b = input().split()
    if not parent.get(a):
      parent[a] = a
      cnt[a] = 1
    if not parent.get(b):
      parent[b] = b
      cnt[b] = 1
    print(union(a, b))