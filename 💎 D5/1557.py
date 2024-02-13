k = int(input())
n = 10**10

mu = [0]*(int(n**0.5)+1)
mu[1] = 1
for i in range(1, int(n**0.5)+1):
  for j in range(2*i, int(n**0.5)+1, i):
    mu[j] -= mu[i]

def sfi_num(n):
  cnt = 0
  i = 1
  while i*i<=n:
    cnt += mu[i]*(n//(i*i))
    i += 1
  return cnt
    
    
start, end = 0, n
while start <= end:
  mid = (start + end) // 2
  if sfi_num(mid) >= k:
    end = mid - 1
  else:
    start = mid + 1

print(start)