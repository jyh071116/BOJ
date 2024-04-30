from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque([])

for _ in range(n):
  command = input().strip()
  try:
    if command[0] == '1':
      cmd, num = command.split()
      q.appendleft(num)
    elif command[0] == '2':
      cmd, num = command.split()
      q.append(num)
    elif command[0] == '3':
      print(q.popleft())
    elif command[0] == '4':
      print(q.pop())
    elif command[0] == '5':
      print(len(q))
    elif command[0] == '6':
      print(int(not len(q)))
    elif command[0] == '7':
      print(q[0])
    elif command[0] == '8':
      print(q[-1])
  except:
    print(-1)