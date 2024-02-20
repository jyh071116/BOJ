t = int(input())

def pow(a, n, mod):
  res = 1
  while n:
    if n % 2 == 1: res = res * a % mod
    n //= 2
    a = a * a % mod
  return res

for i in range(1, t+1):
  a, p = map(int, input().split())
  print(f"Scenario #{i}:")
  if pow(a, (p-1)//2, p) == 1:
    print(1)
  else:
    print(-1)
  print()