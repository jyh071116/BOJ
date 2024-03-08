n, k = map(int, input().split())
prime = [1]*(n+1)
for i in range(2, n+1):
  if prime[i]:
    j = 1
    while i*j <= n:
      if prime[i*j] == 1:
        k -= 1
        if k == 0:
          print(i*j)
          exit()
      prime[i*j] = 0
      j += 1
