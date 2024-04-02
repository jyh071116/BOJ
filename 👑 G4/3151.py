import bisect

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0

for i in range(n-1):
  for j in range(1, n):
    key = -1 * (arr[i] + arr[j])
    lower_bound = bisect.bisect_left(arr, key, i+1, j)
    upper_bound = bisect.bisect_right(arr, key, i+1, j)
    cnt += upper_bound - lower_bound
print(cnt)