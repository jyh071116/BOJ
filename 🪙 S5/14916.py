n = int(input())
dp = [float('inf')]*(100001)
dp[2], dp[4], dp[5] = 1, 2, 1
for i in range(6, 100001):
  dp[i] = min(dp[i-5], dp[i-2])+1

print(dp[n] if dp[n] != float('inf') else -1)