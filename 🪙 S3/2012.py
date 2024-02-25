n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

res = 0
for i in range(n):
  res += abs(arr[i]-(i+1))

print(res)