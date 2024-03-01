k = int(input())
size = 1
cnt = 0
while size < k:
  size *= 2
  cnt += 1

power = cnt
while True:
  if k >= 2**power:
    k -= 2**power
    if k == 0:
      break
  power -= 1

print(size, cnt-power)