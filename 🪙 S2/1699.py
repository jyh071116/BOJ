n = int(input())
dp = [float('inf')]*(n+1)
dp[0], dp[1] = 0, 1

for i in range(3, n+1):
  for j in range(1, int(n**0.5)+1):
    if i >= j*j:
      dp[i] = min(dp[i], dp[i-(j*j)] + 1)

print(dp[n])