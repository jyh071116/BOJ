a = [0] + list(input())
b = [0] + list(input())
dp = [[0]*len(b) for _ in range(len(a))]

for i in range(1, len(a)):
  for j in range(1, len(b)):
    if a[i] == b[j]:
      dp[i][j] = dp[i-1][j-1]+1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

res = []
def backtracking(i, j):
  if dp[i][j] == 0:
    return
  if dp[i-1][j] == dp[i][j]:
    return backtracking(i-1, j)
  if dp[i][j-1] == dp[i][j]:
    return backtracking(i, j-1)
  res.append(a[i])
  return backtracking(i-1, j-1)

backtracking(len(a)-1, len(b)-1)
print(dp[len(a)-1][len(b)-1])
print("".join(reversed(res)))