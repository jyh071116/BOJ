n, m = map(int, input().split())
buy6, buy1 = float('inf'), float('inf')
for _ in range(m):
  a, b = map(int, input().split())
  if a < buy6:
    buy6 = a
  if b < buy1:
    buy1 = b

print(min(buy6*(n//6) + buy1*(n%6), buy6*(n//6+1), buy1*n))