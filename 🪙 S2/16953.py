from collections import deque

a, b = map(int, input().split())
q = deque([(a, 0)])

while q:
  num, depth = q.popleft()
  if num == b:
    print(depth+1)
    exit(0)
  for plus in [num*2, num*10+1]:
    if plus <= b:
      q.append((plus, depth+1))

print(-1)