n = int(input())
arr = []
dp = [[0]*i for i in range(1, n+1)]

for _ in range(n):
  arr.append(list(map(int, input().split())))

def f(a, b):
  if a >= n or b > a:
    return 0
  
  if a == n-1:
    return arr[a][b]
  
  if dp[a][b] != 0:
    return dp[a][b]
  
  dp[a][b] = max(f(a+1, b), f(a+1, b+1)) + arr[a][b]
  return dp[a][b]

print(f(0, 0))