import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
dic = {}
for _ in range(m):
  u, v = map(int, input().split())
  try:
    dic[u].append(v)
  except:
    dic[u] = [v]
  
  try:
    dic[v].append(u)
  except:
    dic[v] = [u]

for i in dic.keys():
  dic[i].sort()
  
visited = [0]*(1+n)
visited[r] = 1
_round = 1

q = deque([r])
while q:
  num = q.popleft()
  
  for i in dic[num]:
    if not visited[i]:
      _round += 1
      visited[i] = _round
      q.append(i)

for i in visited[1:]:
  print(i)