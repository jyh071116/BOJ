n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)
for i in range(n):
  if i + arr[i][0] <= n:
    dp[i+arr[i][0]] = max(dp[i+arr[i][0]], dp[i]+arr[i][1])
    for j in range(i+arr[i][0], n+1):
      dp[j] = max(dp[j], dp[i+arr[i][0]])
print(max(dp))