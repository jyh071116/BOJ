n, m = map(int, input().split())
arr = list(map(int, input().split()))
primes = []
cnt = 0
res = 0

def backtracking(idx):
  global res
  if idx == n:
    if not primes:
      return
    mul = 1
    for prime in primes:
      mul *= prime
    if len(primes) % 2 == 1:
      res += m // mul
    else:
      res -= m // mul
    return
    
  primes.append(arr[idx])
  backtracking(idx+1)
  primes.pop()
  backtracking(idx+1)

backtracking(0)
print(res)