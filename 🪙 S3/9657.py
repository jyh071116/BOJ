n = int(input())
dp = [0]*(1001)
dp[1], dp[2], dp[3], dp[4] = 1, 0, 1, 1

for i in range(5, n+1):
  dp[i] = (min(dp[i-1], dp[i-3], dp[i-4]) + 1) % 2

if dp[n] == 1:
  print("SK")
else:
  print("CY")