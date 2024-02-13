n, k = map(int, input().split())
value = 1

for i in range(2, n+1):
  value = (value + k - 1) % i + 1

print(value)