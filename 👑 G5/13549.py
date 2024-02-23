from collections import deque

n, k = map(int, input().split())
visited = [float('inf')]*(100001)
q = deque([(n, 0)])
min_time = float('inf')

while q:
  x, time = q.popleft()
  if x == k:
    min_time = min(min_time, time)
  
  for pos in [x-1, x+1]:
    if 0<=pos<=100000 and time+1 < visited[pos]:
      visited[pos] = time+1
      q.append((pos, time+1))
  
  if 0<=x*2<=100000 and time < visited[x*2]:
    visited[x*2] = time
    q.append((x*2, time))

print(min_time)