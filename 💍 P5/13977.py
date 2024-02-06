import sys
input = sys.stdin.readline

m = int(input())
p = 1000000007

def power(n, k):
  if k == 0:
    return 1
  if k == 1:
    return n
  temp = power(n, k//2)
  if k%2 == 0:
    return temp**2%p
  if k%2 == 1:
    return temp**2*n%p
  
factorial = [1]*(4000001)

for i in range(2, 4000001):
  factorial[i] = factorial[i-1]*i%p

for _ in range(m):
  n, k = map(int, input().split())
  print(factorial[n] * (power(factorial[k]*factorial[n-k]%p, p-2))%p)