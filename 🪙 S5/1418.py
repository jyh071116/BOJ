n = int(input())
k = int(input())

prime = [1]*(n+1)
for i in range(2, int(n**0.5)+1):
  if prime[i] == 1:
    j = i
    while i*j <= n:
      prime[i*j] = i
      j += 1

def 세준수(n):
  while n != 1:
    if n > k and prime[n] == 1:
      return False
    if prime[n] > k:
      return False
    if prime[n] == 1:
      n //= n
    else:
      n //= prime[n]
  return True

cnt = 0
for i in range(1, n+1):
  if 세준수(i):
    cnt += 1
print(cnt)