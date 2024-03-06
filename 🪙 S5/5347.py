t = int(input())

def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a%b)

def lcm(a, b):
  return a*b // gcd(a, b)

for _ in range(t):
  a, b = map(int, input().split())
  print(lcm(a, b))