t = int(input())

dp = {1:1, 2:2, 3:4}

for _ in range(t):
  n = int(input())
  
  for i in range(4, n+1):
    if i not in dp:
      dp[i] = (dp[i-3] + dp[i-2] + dp[i-1])%1000000009
  
  print(dp[n])