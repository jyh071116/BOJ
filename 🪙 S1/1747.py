_max = 1003001
isPrime = [1]*(_max+1)
isPrime[0], isPrime[1] = 0, 0
n = int(input())

for i in range(2, _max+1):
  if isPrime[i]:
    j = 2
    while i*j <= _max:
      isPrime[i*j] = 0
      j += 1

while True:
  if isPrime[n] and str(n) == str(n)[::-1]:
    print(n)
    break
  n += 1