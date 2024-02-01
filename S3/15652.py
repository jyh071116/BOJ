n, m = map(int, input().split())

def f(arr):
  if len(arr) == m:
    print(*arr)
    return
  for i in range(1, n+1):
    try:
      maxArr = max(arr)
    except:
      maxArr = 0
    
    if i >= maxArr:
      f(arr + [i])

f([])