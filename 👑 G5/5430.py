import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  p = list(input())
  n = int(input())
  temp = input().strip()
  if temp == "[]":
    arr = deque([])
  else:
    arr = deque(list(map(int, temp[1:-1].split(","))))
  isReversed = False
  for i in p:
    if i == "R":
      isReversed = not isReversed
    elif i == "D":
      if len(arr) == 0:
        break
      if isReversed:
        arr.pop()
      else:
        arr.popleft()
  else:
    if isReversed:
      res = "["
      for i in reversed(arr):
        res += f'{i},'
    else:
      res = "["
      for i in arr:
        res += f'{i},'
    print("[]" if len(res) == 1 else res[:-1] + "]")
    continue
  print("error")