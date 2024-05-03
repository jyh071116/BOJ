t = int(input())
_max = int((4*10**12)**0.5)+1
isPrime = [1]*(_max+1)

for i in range(2, int(_max**0.5)+1):
  if isPrime[i]:
    j = 2
    while i*j <= _max:
      isPrime[i*j] = 0
      j += 1

def checkPrime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5)+1):
    if isPrime[i] and n % i == 0:
      return False
  return True

for _ in range(t):
  a, b = map(int, input().split())
  if a+b != 2 and (a+b) % 2 == 0:
    print("YES")
  else:
    if checkPrime(a+b-2):
      print("YES")
    else:
      print("NO")