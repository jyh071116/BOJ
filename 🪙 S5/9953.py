import sys
input = sys.stdin.readline

while True:
  n = int(input())
  if n == 0:
    break
  arr = []
  cnt = 0
  if n % 2 == 0:
    for i in range(1, 51):
      arr.append(2*i)
  else:
    cnt += 1
    for i in range(1, 51):
      arr.append(i*2-1)
  start, end = 0, 49
  while start <= end:
    mid = (start + end) // 2
    cnt += 1
    if arr[mid] == n:
      break
    if arr[mid] > n:
      end = mid - 1
    else:
      start = mid + 1
  print(cnt)