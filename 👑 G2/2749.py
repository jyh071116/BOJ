n = int(input())
m = 10**6
cycle = 15*(m//10)

dp = [0]*(cycle+1)
dp[1] = 1

for i in range(2, cycle+1):
  dp[i] = (dp[i-2] + dp[i-1]) % m

print(dp[n % cycle])