n, k = map(int, input().split())
comb = [[0]*30 for _ in range(30)]
for i in range(30):
  comb[i][0] = 1
  comb[i][i] = 1
for i in range(2, 30):
  for j in range(1, i):
    comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
print(comb[n-1][k-1])