n = int(input())
res = n*2-1

i = 2
while i < n:
  j = ((n-1)//((n-1)//i))
  res += (n-1)//i * (j-i+1)
  i = j+1

print(res)