t = int(input())

for _ in range(t):
  n = int(input())
  if n == 1:
    print(0)
  elif n % 2 == 0:
    print('1'*n)
  else:
    if n % 4 == 3:
      print('1'*(n//2) + '2' + '1'*(n//2))
    else:
      print('1'*(n//2) + '0' + '1'*(n//2))