n = int(input())
dp = {}

def f(n):
  if n == 0:
    return 1
  if n in dp:
    return dp[n]
  res = 0
  for i in range(n):
    res += f(i) * f(n-i-1)
  dp[n] = res
  return dp[n]

print(f(n))