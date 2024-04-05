k = int(input())
_max = 7368787
isPrime = [1]*(_max+1)
for i in range(2, int(_max**0.5)+1):
  if isPrime[i]:
    j = 2
    while i*j <= _max:
      isPrime[i*j] = 0
      j += 1

cnt = 0
for i in range(2, _max+1):
  if isPrime[i]:
    cnt += 1
  if cnt == k:
    print(i)
    break