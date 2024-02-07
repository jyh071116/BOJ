n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [float('inf')]*(k+1)
dp[0] = 0

for i in range(1, k+1):
  lst = [dp[i-coin] for coin in coins if i >= coin]
  if lst:
    dp[i] = min(lst) + 1

if dp[k] == float('inf'):
  print(-1)
else:
  print(dp[k])