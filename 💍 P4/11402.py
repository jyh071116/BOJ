n, k, m = map(int, input().split())
comb = [[0]*m for _ in range(m)]

for i in range(m):
  comb[i][0] = 1
  for j in range(1, i+1):
    comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % m

res = 1
while n or k:
  res = res * comb[n%m][k%m] % m
  n //= m
  k //= m

print(res)