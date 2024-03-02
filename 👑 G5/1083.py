n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n):
  idx = arr.index(max(arr[i: min(n, i+s+1)]))
  
  for j in range(idx, i, -1):
    arr[j], arr[j-1] = arr[j-1], arr[j]
  
  s -= idx-i
  if s <= 0: break
print(*arr)