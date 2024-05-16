import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
lecture = [list(map(int, input().split())) for _ in range(n)]
lecture.sort(key=lambda x: (x[1], x[2]))
lectureroom = [lecture[0][2]]
heapify(lectureroom)

for i in range(1, n):
  if lecture[i][1] >= lectureroom[0]:
    heappop(lectureroom)
  heappush(lectureroom, lecture[i][2])

print(len(lectureroom))