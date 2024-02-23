from collections import deque

n, k = map(int, input().split())
cnt = 0
min_time = float('inf')
visited = {}

q = deque([(n, 0)])

while q:
  x, time = q.popleft()
  if x == k:
    if time == min_time:
      cnt += 1
    elif time < min_time:
      min_time = time
      cnt = 1
    continue
  if time >= min_time:
    continue
  
  for pos in [x-1, x+1, x*2]:
    if 0<=pos<=100000:
      try:
        if time + 1 <= visited[pos]:
          visited[pos] = time + 1
          q.append((pos, time+1))
      except:
        visited[pos] = time + 1
        q.append((pos, time+1))

print(min_time)
print(cnt)