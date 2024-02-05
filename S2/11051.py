import sys
sys.setrecursionlimit(10**9)

n, k = map(int, input().split())
dp = [[None]*(k+1) for _ in range(n+1)]

def comb(n, k):
  if n==k or k==0:
    return 1
  
  if dp[n][k] != None:
    return dp[n][k]
  
  dp[n][k] = (comb(n-1, k-1) + comb(n-1, k))%10007
  return dp[n][k]

print(comb(n, k))