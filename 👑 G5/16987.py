n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_cnt = 0

def backtracking(index):
  global max_cnt
  
  if index == n:
    max_cnt = max(max_cnt, len([1 for i in arr if i[0] <= 0]))
    return
  
  if arr[index][0] <= 0 or len([1 for i in range(n) if arr[i][0] > 0 and i != index]) == 0:
    return backtracking(index+1)
  
  for i in range(n):
    if i != index and arr[i][0] > 0:
      arr[index][0] -= arr[i][1]
      arr[i][0] -= arr[index][1]
      backtracking(index+1)
      arr[index][0] += arr[i][1]
      arr[i][0] += arr[index][1]

backtracking(0)
print(max_cnt)