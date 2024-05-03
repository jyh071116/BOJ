n, m = map(int, input().split())
p = 1000000007

def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a%b)
 
gcd_n_m = gcd(n, m)

fibo = {}
def fibonacci(n) :
  if n == 0:
    return 0
  if n == 1 or n == 2:
    fibo[n] = 1
    return fibo[n]
  if n in fibo:
    return fibo[n]

  if n & 1:
    k = (n+1)//2
    fibo[n] = (fibonacci(k)*fibonacci(k) + fibonacci(k-1) * fibonacci(k-1)) % p
  else :
    k = n//2
    fibo[n] = (2*fibonacci(k-1) + fibonacci(k)) * fibonacci(k) % p

  return fibo[n]
print(fibonacci(gcd_n_m))