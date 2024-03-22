import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([])
for _ in range(n):
  temp = input().strip().split()
  if temp[0] == "push":
    q.append(temp[1])
  elif temp[0] == "pop":
    if not q:
      print(-1)
    else:
      print(q.popleft())
  elif temp[0] == "front":
    if not q:
      print(-1)
    else:
      print(q[0])
  elif temp[0] == "back":
    if not q:
      print(-1)
    else:
      print(q[-1])
  elif temp[0] == "size":
    print(len(q))
  elif temp[0] == "empty":
    print(int(not q))