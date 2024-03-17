a = [0] + list(input())
b = [0] + list(input())
dp = [[0]*len(b) for _ in range(len(a))]

for i in range(1, len(a)):
  for j in range(1, len(b)):
    if a[i] == b[j]:
      dp[i][j] = dp[i-1][j-1]+1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

_max = 0
for i in range(len(a)):
  for j in range(len(b)):
    _max = max(_max, dp[i][j])
print(_max)