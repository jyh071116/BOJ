n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]

for i in range(m):
  arr[0][i] = 1

for i in range(n):
  arr[i][0] = 1

for i in range(1, n):
  for j in range(1, m):
    arr[i][j] = (arr[i-1][j] + arr[i][j-1] + arr[i-1][j-1]) % 1000000007

print(arr[n-1][m-1])