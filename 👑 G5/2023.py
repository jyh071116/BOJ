n = int(input())
def isPrime(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

res = []
def backtracking(idx, num):
  if idx == n:
    res.append(num)
    return
  for i in [1, 3, 5, 7, 9]:
    if isPrime(num*10+i):
      backtracking(idx+1, num*10+i)

for i in [2, 3, 5, 7]:
  backtracking(1, i)
for i in res:
  print(i)