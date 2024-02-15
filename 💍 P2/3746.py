import sys

max_val = 10**4

mu = [0]*(max_val+1)
mu[1] = 1
for i in range(1, max_val+1):
  for j in range(2*i, max_val+1, i):
    mu[j] -= mu[i]

lines = sys.stdin.readlines()
for line in range(0, len(lines), 2):
  n = int(lines[line])
  arr = [0]*(max_val+1)
  for i in map(int, lines[line+1].split()):
    arr[i] += 1
    
  cnt = 0
  for i in range(1, max_val+1):
    multiple = arr[i]
    for j in range(i*2, max_val+1, i):
      multiple += arr[j]
    cnt += mu[i] * multiple * (multiple - 1) * (multiple - 2) * (multiple - 3) // 24
  print(cnt)