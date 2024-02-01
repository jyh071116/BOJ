n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

def f(arr):
  if len(arr) == m:
    print(*arr)
    return
  for i in lst:
    if not i in arr:
      f(arr + [i])

f([])