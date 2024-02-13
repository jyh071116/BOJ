from collections import deque

n = int(input())
visited = {n: 1}

q = deque([(n, 0)])

while q:
  n, depth = q.popleft()
  if n == 1:
    print(depth)
    break
  
  if n % 3 == 0 and not n//3 in visited:
    visited[n//3] = 1
    q.append((n//3, depth+1))
    
  if n % 2 == 0 and not n//2 in visited:
    visited[n//2] = 1
    q.append((n//2, depth+1))
  
  if not n-1 in visited:
    visited[n-1] = 1
    q.append((n-1, depth+1))