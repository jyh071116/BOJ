n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = {}
def backtracking(lst, last):
  if len(lst) == m:
    ans[f'{lst}'] = 1
    return
  
  for i in range(n):
    if i not in last:
      backtracking(lst + [arr[i]], last + [i])

backtracking([], [])
for item in ans.keys():
  print(item[1:-1].replace(",", ""))