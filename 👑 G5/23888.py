import sys
input = sys.stdin.readline

a, d = map(int, input().split())

def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a%b)

def sum(n):
  return (n*(2*a+(n-1)*d))//2

q = int(input())
for _ in range(q):
  op, l, r = map(int, input().split())
  if op == 1:
    print(sum(r)-sum(l-1))
  else:
    if l == r or d == 0:
      print(a+(l-1)*d)
    else:
      print(gcd(a, d))