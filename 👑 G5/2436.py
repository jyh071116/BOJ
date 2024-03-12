def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a%b)

a, b = map(int, input().split())
val = int((a*b)**0.5)
min = [float('inf'), float('inf'), float('inf')]
for i in range(val - (val%a), 0, -a):
  if gcd(i, a*b//i) == a and a*b % i == 0 and i + a*b//i < min[2]:
    min = [i, a*b//i, i + a*b//i]

print(min[0], min[1])