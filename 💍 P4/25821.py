a, b = map(int, input().split())
lst = [2, 3, 5, 7, 11]
cnt = 0
for i in lst:
  if a <= i <= b:
    cnt += 1

def power(a, n, mod):
  res = 1
  while n:
    if n % 2 == 1:
      res = res * a % mod
    n //= 2
    a = a * a % mod
  return res

def miller(a, n):
  if a % n == 0:
    return True
  k = n-1
  while True:
    temp = power(a, k, n)
    if temp == n-1:
      return True
    if k % 2 == 1:
      return (temp == 1 or temp == n-1)
    k //= 2

for i in range(10, 10**6):
  if int(str(i)[0]) % 2 == 0: continue
  i = int(str(i) + str(i)[-2::-1])
  if a <= i <= b:
    for a in lst:
      if not miller(a, i):
        break
    else:
      cnt += 1
  
print(cnt)