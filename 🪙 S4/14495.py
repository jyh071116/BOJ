n = int(input())
dp = [0]*117
dp[1], dp[2], dp[3] = 1, 1, 1
for i in range(4, 117):
  dp[i] = dp[i-3] + dp[i-1]
print(dp[n])