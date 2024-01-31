n, k = map(int, input().split())
arr = []

def dfs(box: [int]):
  if sum(box) == n:
    arr.append(box)
    return
  if sum(box) > n:
    return
  for i in [1, 2, 3]:
    dfs(box + [i])

dfs([])
if len(arr) < k:
  print(-1)
else: 
  print("+".join(map(str, arr[k-1])))