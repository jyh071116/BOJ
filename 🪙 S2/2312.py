t = int(input())
isPrime = [1]*100001
for i in range(2, 100001):
  if isPrime[i]:
    j = 2
    while i*j <= 100000:
      isPrime[i*j] = 0
      j += 1
      
for _ in range(t):
  n = int(input())
  dic = {}
  while n != 1:
    for i in range(2, n+1):
      if isPrime[i] and n % i == 0:
        n //= i
        try:
          dic[i] += 1
        except:
          dic[i] = 1
        break
  for i in dic.keys():
    print(i, dic[i])