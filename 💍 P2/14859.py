n = int(input())
max = 10**6
arr = [0]*(max+1)
for i in map(int, input().split()):
  arr[i] += 1
cnt = 0

mu = [0]*(max+1)
mu[1] = 1
for i in range(1, max+1):
  multiple = arr[i]
  for j in range(2*i, max+1, i):
    multiple += arr[j]
    mu[j] -= mu[i]
  
  cnt += mu[i] * multiple * (multiple - 1) * (multiple - 2) // 6

print(cnt)