from collections import deque

n, k = map(int, input().split())

q = deque([(n, 0)])
visited = [0]*100001
visited[n] = 1
move = [0]*100001

while q:
  x, time = q.popleft()
  if x == k:
    print(time)
    break
  
  for pos in [x-1, x+1, x*2]:
    if 0<=pos<=100000 and not visited[pos]:
      move[pos] = x
      visited[pos] = 1
      q.append((pos, time+1))

temp = move[k]
arr = [k]
for _ in range(time):
  arr.append(temp)
  temp = move[temp]

print(*arr[::-1])