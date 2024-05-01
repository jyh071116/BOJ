n = int(input())
arr = [int(input()) for _ in range(n)]
cnt = 0

while max(arr) != arr[0]:
  arr[arr.index(max(arr))] -= 1
  arr[0] += 1
  cnt += 1

if arr.count(max(arr)) >= 2:
  cnt += 1

print(cnt)