from bisect import bisect_left

n = int(input())
a = list(reversed(list(map(int, input().split()))))
dp = [1]
x = [a[0]]

for i in range(1, n):
  if a[i] > x[-1]:
    x.append(a[i])
    dp.append(dp[-1]+1)
  else:
    idx = bisect_left(x, a[i])
    x[idx] = a[i]

print(dp[-1])