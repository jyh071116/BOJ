n = int(input())
prev, now = 1, 2
for _ in range(n-2):
  prev, now = now%10, (prev+now)%10
print(now)