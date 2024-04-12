t = int(input())

def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a%b)
for _ in range(t):
  arr = list(map(int, input().split()))
  _sum = 0
  for i in range(1, arr[0]+1):
    for j in range(i+1, arr[0]+1):
      _sum += gcd(arr[i], arr[j])
  print(_sum)