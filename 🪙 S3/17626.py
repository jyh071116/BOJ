n = int(input())
dp = [float('inf')]*(n+1)

for i in range(1, n+1):
  if int(i**0.5)**2 == i:
    dp[i] = 1
    continue
  for j in range(1, int(i**0.5)+1):
    dp[i] = min(dp[i], dp[i-j*j]+1)
print(dp[n])