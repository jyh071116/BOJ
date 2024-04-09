def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a%b)

a, b = map(int, input().split())
c, d = map(int, input().split())
분자 = (a*d)+(b*c)
분모 = b*d
gcd = gcd(분자, 분모)
print(분자//gcd, 분모//gcd)