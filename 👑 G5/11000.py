import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
lecture = [list(map(int, input().split())) for _ in range(n)]
lecture.sort(key=lambda x: (x[0], x[1]))
lectureroom = [lecture[0][1]]
heapify(lectureroom)

for i in range(1, n):
  if lecture[i][0] >= lectureroom[0]:
    heappop(lectureroom)
  heappush(lectureroom, lecture[i][1])

print(len(lectureroom))