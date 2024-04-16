n, m = map(int, input().split())
p = 1000000007
factorial = [1]*(1000001)
for i in range(2, 1000001):
  factorial[i] = i * factorial[i-1] % p
print(factorial[n]*pow(factorial[n-m]*factorial[m], p-2, p)%p)