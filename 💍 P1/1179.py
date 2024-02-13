import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())

def f(n, k):
  if n == 1:
    return 0
  if k == 1:
    return n-1
  if 1 < n < k:
    return (f(n-1, k) + k) % n
  
  h = f(n-(n//k), k) - (n % k)
  if h < 0:
    h += n
  else:
    h += h//(k-1)
  return h

print(f(n, k)+1)