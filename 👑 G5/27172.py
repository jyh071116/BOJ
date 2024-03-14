n = int(input())
arr = list(map(int, input().split()))
s = set(arr)
m = max(arr)
score = [0]*(m+1)

for i in arr:
  j = 2
  while i*j <= m:
    if i*j in s:
      score[i] += 1
      score[i*j] -= 1
    j += 1

for i in arr:
  print(score[i], end=" ")