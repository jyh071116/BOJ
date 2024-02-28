n = int(input())
dp = [0]*(1001)
dp[1], dp[2], dp[3], dp[4], dp[5] = 0, 1, 0, 1, 1

for i in range(6, n+1):
  if dp[i-1] == 1 and dp[i-3] == 1 and dp[i-4] == 1: dp[i] = 0
  else: dp[i] = 1

if dp[n] == 1:
  print("SK")
else:
  print("CY")