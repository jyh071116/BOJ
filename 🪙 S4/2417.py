n = int(input())
q = int(n**0.5)
while q*q < n:
  q += 1
print(q)