n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

def f(arr):
  if len(arr) == m:
    print(*arr)
    return
  for i in lst:
    try:
      maxArr = arr[-1]
    except:
      maxArr = 0
    
    if i >= maxArr:
      f(arr + [i])
      
f([])