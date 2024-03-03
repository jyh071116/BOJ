n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()
max_val = 0
for i in range(n):
  max_val = max(ropes[i]*(n-i), max_val)
print(max_val)