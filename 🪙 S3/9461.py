t = int(input())
dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0]*(91)

for i in range(11, 101):
  dp[i] = dp[i-5] + dp[i-1]

for i in range(t):
  n = int(input())
  print(dp[n])