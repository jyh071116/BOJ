a, b, L = map(int, input().split())
L약수 = set([])
for i in range(1, int(L**(0.5))+1):
  if L%i==0:
    L약수.add(i)
    L약수.add(L//i)

L약수 = sorted(list(L약수))
    
def gcd(a, b):
  if a%b == 0: return b
  return gcd(b, a%b)

def lcm(a, b):
  return (a*b) / gcd(a,b)

a_b_lcm = lcm(a, b)
ans = -1
for c in L약수:
  if lcm(a_b_lcm, c) == L:
    print(c)
    break
else:
  print(-1)