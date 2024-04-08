n = int(input())
k = int(input())
arr = [int(input()) for _ in range(n)]
dic = {}

def backtracking(cnt, idxArr):
  if cnt == k:
    dic["".join(map(str, [arr[i] for i in idxArr]))] = 1
    return
  for i in range(n):
    if i not in idxArr:
      backtracking(cnt+1, idxArr + [i])

backtracking(0, [])
print(len(dic))