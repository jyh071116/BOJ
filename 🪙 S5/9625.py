k = int(input())

fibo = [0]*46
fibo[1] = 1
for i in range(2, 46):
  fibo[i] = fibo[i-2] + fibo[i-1]

if k == 0:
  print(1, fibo[k])
else:
  print(fibo[k-1], fibo[k])