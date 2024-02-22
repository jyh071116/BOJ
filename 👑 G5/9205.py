from collections import deque

t = int(input())
for _ in range(t):
  n = int(input())
  x, y = list(map(int, input().split()))
  convenient = [list(map(int, input().split())) for _ in range(n)]
  rock = list(map(int, input().split()))
  visited = {}
  
  q = deque([(x, y)])
  while q:
    x, y = q.popleft()
    if abs(rock[0]-x) + abs(rock[1]-y) <= 1000:
      print("happy")
      break
    
    for a, b in convenient:
      if (a, b) not in visited and abs(a-x) + abs(b-y) <= 1000:
        visited[(a, b)] = 1
        q.append((a, b))
  else:
    print("sad")