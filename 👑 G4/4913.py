_max = 1000000
isPrime = [1]*(_max+1)
isPrime[0], isPrime[1] = 0, 0
for i in range(2, int(_max**0.5)):
  if isPrime[i]:
    j = 2
    while i*j <= _max:
      isPrime[i*j] = 0
      j += 1

prime_sum = [0]*(_max+1)
square_sum = [0]*(_max+1)
for i in range(2, _max+1):
  if isPrime[i]:
    prime_sum[i] = prime_sum[i-1] + 1
    if i == 2 or i % 4 == 1:
      square_sum[i] = square_sum[i-1] + 1
      continue
    square_sum[i] = square_sum[i-1]
  else:
    prime_sum[i] = prime_sum[i-1]
    square_sum[i] = square_sum[i-1]
      
while True:
  l, u = map(int, input().split())
  if l == -1 and u == -1:
    break
  print(l, u, prime_sum[max(0, u)] - prime_sum[max(0, l-1)], square_sum[max(0, u)] - square_sum[max(0, l-1)])