s = int(input())
n = 0
sum = 0
while True:
  sum += n
  if sum > s:
    print(n-1)
    break
  n += 1