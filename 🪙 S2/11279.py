import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
  a = int(input())
  if a == 0:
    if not arr:
      print(0)
    else:
      print(heapq.heappop(arr)[1])
  else:
    heapq.heappush(arr, (-a, a))