n, s = map(int, input().split())
arr = list(map(int, input().split())) + [0, 0]

start = 0
end = 0
length = 1
sum = arr[0]
res = float('inf')

while end <= n:
  if sum < s:
    end += 1
    length += 1
    sum += arr[end]
  else:
    res = min(res, length)
    sum -= arr[start]
    start += 1
    length -= 1

if res == float('inf'):
  print(0)
else:
  print(res)