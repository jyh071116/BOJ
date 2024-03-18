import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
arr = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
  if i <= n-2 and lst[i] == lst[i+1]:
    arr[i][i+1] = 1
  arr[i][i] = 1

for i in range(n-1, -1, -1):
  for j in range(i, n):
    if lst[i] == lst[j] and arr[i+1][j-1]:
      arr[i][j] = 1

for _ in range(m):
  s, e = map(int, input().split())
  print(arr[s-1][e-1])