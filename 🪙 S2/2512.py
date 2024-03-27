n = int(input())
arr = list(map(int, input().split()))
_max = int(input())
start, end = 0, max(arr)

while start <= end:
  mid = (start + end) // 2
  _sum = sum([i if i <= mid else mid for i in arr])
  if _sum == _max:
    print(mid)
    exit()
  if _sum > _max:
    end = mid - 1
  else:
    start = mid + 1
print(end)